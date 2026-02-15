import sqlite3

DB="memory.db"

def connect():
    return sqlite3.connect(DB)


def save_memory(user, assistant):

    conn=connect()
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        assistant TEXT
    )
    """)

    cur.execute(
        "INSERT INTO chat_history(user,assistant) VALUES (?,?)",
        (user,assistant)
    )

    conn.commit()
    conn.close()


def load_memory(limit=5):

    conn=connect()
    cur=conn.cursor()

    cur.execute("""
    SELECT user,assistant
    FROM chat_history
    ORDER BY id DESC
    LIMIT ?
    """,(limit,))

    rows=cur.fetchall()
    conn.close()

    return rows[::-1]
