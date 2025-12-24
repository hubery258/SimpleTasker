import sqlite3
from pathlib import Path

SQL = """CREATE TABLE IF NOT EXISTS tasks (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         ddl TEXT,
         content TEXT,
         duration INTEGER NOT NULL,
         quadrant INTEGER NOT NULL,
         completed INTEGER NOT NULL DEFAULT 0
     );"""


def main():
    db_path = Path("task.db")
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute(SQL)
    conn.commit()
    conn.close()
    print(f"Ensured 'tasks' table exists in {db_path}")


if __name__ == "__main__":
    main()
