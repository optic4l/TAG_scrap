import sqlite3


def create_tables():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute("""
            CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY UNIQUE,
            username TEXT
            )
          """)
    c.execute("""
            CREATE TABLE IF NOT EXISTS patentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            patente TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
            UNIQUE(user_id, patente)
            )
          """)
    conn.commit()
    conn.close()

def add_user(chat_id, username):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (chat_id, username))
    conn.commit()
    conn.close()

def get_chat_id(username):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def add_patente(user_id, patente):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute("INSERT OR IGNORE INTO patentes (user_id, patente) VALUES (?, ?)", (user_id, patente))
    conn.commit()
    conn.close()

