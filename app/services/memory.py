import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.getcwd(), 'data', 'chat_history.db')

def init_db():
    """Initializes the SQLite database table for conversation history."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def save_message(session_id: str, role: str, content: str):
    """Saves a single message (user or assistant) to the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (session_id, role, content, timestamp) VALUES (?, ?, ?, ?)",
            (session_id, role, content, datetime.utcnow())
        )
        conn.commit()

def get_recent_history(session_id: str, limit: int = 5) -> list[dict]:
    """
    Retrieves the last N messages for a given session in chronological order (sliding window).
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT role, content, timestamp FROM messages
            WHERE session_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (session_id, limit)
        )
        rows = cursor.fetchall()
        
    # Reverse to return chronological order
    history = [{"role": row[0], "content": row[1], "timestamp": row[2]} for row in reversed(rows)]
    return history
