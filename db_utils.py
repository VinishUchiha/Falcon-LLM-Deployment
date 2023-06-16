import sqlite3

def create_table(db_name = 'api_key.db', table_name = 'API_KEY_HASH'):
    conn= sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")

    table = f""" CREATE TABLE {table_name} (
                USER_NAME VARCHAR(255) NOT NULL,
                HASH VARCHAR(255) NOT NULL
            ); """
    cur.execute(table)
    conn.commit()
    conn.close()