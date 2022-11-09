#!/usr/bin/env python3

import secrets, argparse, sys, base64, os, getpass
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def main():
    password_provided = getpass.getpass(prompt=str("Password: "))
    password = password_provided.encode()

    salt = b'\xbc\n\xd6\xa1\xfb(_\xf8[\n\xe5<\xa7\x04J\xaa'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    while True: 
        try:
            f = Fernet(key)
            db = open('/home/user/Documents/Programming/PasswordManager/database.txt')
            encrypted = db.read().encode()
            decrypted = decrypted = f.decrypt(encrypted)
            original_message = decrypted.decode()
            db.close()
        except:
            print("Invalid password.")
            break

        parser = argparse.ArgumentParser(description = "A CLI tool made in Python to manage your passwords.")

        # List of command arguments
        parser.add_argument("-a", "--add", help = "Create a new entry", action="store_true")
        parser.add_argument("-r", "--remove", help = "Remove an entry", action="store_true")
        parser.add_argument("-v", "--view", help = "View the database", action="store", nargs="+")

        # Variable containing parsed user arguments
        args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

        # Defined characters for password generation
        ascii_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        unicode_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

        if args.add: 
            add_to_database(original_message, ascii_chars, unicode_chars, f)
            break
        elif args.remove:
            remove_from_database()
            break
        elif args.view:
            view_database(args, original_message)
            break

def add_to_database(original_message, ascii_chars, unicode_chars, f):
    website = input("Website URL:\n>>> ")
    user = input("Email:\n>>> ")
    length = int(input("Please select a password length: "))
    password_type = int(input("Password Type:\n1: Alphanumeric\n2: Unicode Inclusive\n>>> "))
    while True:
        if password_type == 1:
            password = ''.join(secrets.choice(ascii_chars) for i in range(length))
        elif password_type == 2:
            password = ''.join(secrets.choice(unicode_chars) for i in range(length))
        else:
            print("Invalid type.")
            break
        print("\nYour password is:\n" + password)
        accept = int(input("1: Regenerate\n2: Add to Database\n>>> "))
        if accept == 1:
            continue
        elif accept == 2:
            try:
                new_message = (original_message + "site:" + website + "\nmail:" + user + "\npwd:" + password + "\n\n")
                encoded = new_message.encode()
                encrypted = f.encrypt(encoded)
                file = open('/home/user/Documents/Programming/PasswordManager/database.txt', 'wb')
                file.write(encrypted)
                file.close()
                print("Information added to database.")
                break
            except ValueError:
                print("An error has occurred. Please try again.")
                break
        else:
            print("Program aborted.")
            break

def remove_from_database():
    pass

def view_database(args, original_message):
    if args.view[0] == "all" and len(args.view) == 1:
        print(original_message)
    elif args.view[0] == "site" and len(args.view) == 2:
        pass
    elif args.view[0] == "mail" and len(args.view) == 2:
        pass
    else:
        parser.error("argument -v/--view: invalid argument(s), expected [\"all\"], [\"site\",\"value\"], or [\"mail\",\"value\"]")

if __name__ == "__main__":
    main()
