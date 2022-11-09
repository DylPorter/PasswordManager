# PasswordManager 0.1

A simple CLI (Command-Line Interface) password manager for Linux/UNIX created in [Python 3.10.8](https://www.python.org/downloads/).

Encrypted using SHA-256 in the [cryptography](https://pypi.org/project/cryptography/) library, password protected using the [getpass](https://docs.python.org/3/library/getpass.html) library.

<br>

**DISCLAIMER:**
  
**A `database.txt` file is automatically created, the file is _safe_ and _encrypted_, but PLEASE LEAVE IT UNTOUCHED!**
  
**The `password_manager.py` and `database.txt` file must be kept in the same directory or folder at all times.**


---

### Commands
* pwdmgr -h, --help
* pwdmgr -a, --add
* pwdmgr -r, --remove (TBA)
* pwdmgr -v [arg], --view [arg] (only current argument is "all")
