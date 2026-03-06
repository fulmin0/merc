import sqlite3
from contextlib import contextmanager
from datetime import datetime

DB_PATH = "assistant.db"


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT DEFAULT 'medium',
                status TEXT DEFAULT 'pending',
                due_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                tags TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def create_task(title, description=None, priority="medium", due_date=None):
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority, due_date) VALUES (?, ?, ?, ?)",
            (title, description, priority, due_date),
        )
        return cursor.lastrowid


def list_tasks(status="pending"):
    with get_db() as conn:
        if status == "all":
            rows = conn.execute(
                "SELECT * FROM tasks ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 ELSE 3 END, created_at"
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM tasks WHERE status = ? ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 ELSE 3 END, created_at",
                (status,),
            ).fetchall()
        return [dict(row) for row in rows]


def complete_task(task_id):
    with get_db() as conn:
        conn.execute(
            "UPDATE tasks SET status = 'completed', updated_at = ? WHERE id = ?",
            (datetime.now().isoformat(), task_id),
        )
        return True


def update_task(task_id, **kwargs):
    if not kwargs:
        return False
    fields = ", ".join(f"{k} = ?" for k in kwargs)
    values = list(kwargs.values()) + [datetime.now().isoformat(), task_id]
    with get_db() as conn:
        conn.execute(
            f"UPDATE tasks SET {fields}, updated_at = ? WHERE id = ?", values
        )
        return True


def delete_task(task_id):
    with get_db() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        return True


def create_note(content, tags=None):
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO notes (content, tags) VALUES (?, ?)", (content, tags)
        )
        return cursor.lastrowid


def list_notes():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM notes ORDER BY created_at DESC LIMIT 20"
        ).fetchall()
        return [dict(row) for row in rows]


def get_conversation_history(conversation_id, limit=20):
    with get_db() as conn:
        rows = conn.execute(
            "SELECT role, content FROM conversations WHERE conversation_id = ? ORDER BY created_at DESC LIMIT ?",
            (conversation_id, limit),
        ).fetchall()
        return list(reversed([dict(row) for row in rows]))


def save_message(conversation_id, role, content):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO conversations (conversation_id, role, content) VALUES (?, ?, ?)",
            (conversation_id, role, content),
        )
