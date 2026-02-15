import sqlite3
from config import DB_NAME

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn=connect()
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


def save(role,message):
    conn=connect()
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO chat_history(role,message) VALUES(?,?)",
        (role,message)
    )
    conn.commit()
    conn.close()


def load_history(limit=10):
    conn=connect()
    cur=conn.cursor()
    cur.execute(
        "SELECT role,message FROM chat_history ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows=cur.fetchall()
    conn.close()
    return rows[::-1]

def search_knowledge(query):
    conn=connect()
    cur=conn.cursor()

    cur.execute("""
    SELECT * FROM knowledge
    WHERE rowid IN (
        SELECT rowid FROM knowledge
        WHERE knowledge MATCH ?
        LIMIT 3
    )
    """,(query,))

    rows=cur.fetchall()
    conn.close()

    return rows

