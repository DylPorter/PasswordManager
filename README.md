# PasswordManager

A simple CLI (Command-Line Interface) password manager for Linux/UNIX created in Python 3.10.8.

Encrypted using SHA-256 in the cryptography¹ library, password protected using the getpass² library.

¹ cryptography: https://docs.python.org/3/library/getpass.html
² getpass: https://docs.python.org/3/library/getpass.html

# Commands
pwdmgr -h, --help
pwdmgr -a, --add
pwdmgr -r, --remove (TBA)
pwdmgr -v [arg], --view [arg] (only current argument is "all")
