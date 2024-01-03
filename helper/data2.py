import sqlite3

db_base = sqlite3.connect('data/main.db')


def get_location(cid):
    x = db_base.execute(f"SELECT * FROM users WHERE cid={cid}")
    return x.fetchone()[1]