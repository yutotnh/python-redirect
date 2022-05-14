#!/use/bin/env python3
from getpass import getpass
import os

if os.isatty(0):
    username = input("Username: ")
    password = getpass("Password: ")
else:
    import sys

    username = sys.stdin.readline().rstrip("\n")
    password = sys.stdin.readline().rstrip("\n")

print("Username:", username)
print("Password:", password)
