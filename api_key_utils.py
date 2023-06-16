import time
import hashlib
import base64
from dotenv import dotenv_values
import sqlite3

config = dotenv_values(".env")
SECRET_KEY = config['SECRET_KEY']
DB_NAME = config['DB_NAME']
TABLE_NAME = config['TABLE_NAME']

conn= sqlite3.connect(DB_NAME)
cur = conn.cursor()

def generate_hash(key):
    m = hashlib.sha256()
    m.update(bytes(key, encoding="ascii"))
    m.update(bytes(SECRET_KEY, encoding="ascii"))
    return m.hexdigest()

def generate_key(username):
    curr_time = time.time_ns()
    key_str = f"{username}:{curr_time}"
    key_str_bytes = key_str.encode("ascii")
    base64_bytes = base64.b64encode(key_str_bytes)
    generated_api_key = base64_bytes.decode("ascii")
    generated_hash = generate_hash(key_str)
    cur.execute(f"INSERT INTO API_KEY_HASH  VALUES ('{username}', '{generated_hash}')")
    conn.commit()
    return generated_api_key

def validate_key(api_key):
    try:
        base64_bytes = api_key.encode("ascii")
        key_bytes = base64.b64decode(base64_bytes)
        key_str = key_bytes.decode("ascii")
        generated_hash = generate_hash(key_str)
        username = key_str.split(':')[0]
        cur.execute(f"select HASH from API_KEY_HASH where USER_NAME='{username}'")
        conn.commit()
        hashes = cur.fetchall()
        if generated_hash in [h[0] for h in hashes]:
            return True, username
        else:
            return False, None
    except:
        return False, None

def revoke_key(api_key):
    try:
        base64_bytes = api_key.encode("ascii")
        key_bytes = base64.b64decode(base64_bytes)
        key_str = key_bytes.decode("ascii")
        generated_hash = generate_hash(key_str)
        cur.execute(f"DELETE from API_KEY_HASH where HASH='{generated_hash}'")
        conn.commit()
        print('api key revoked sucessfully')
        return True
    except:
        print('No such api key found')
        return False