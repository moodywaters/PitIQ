# Data
import sqlite3
from datetime import datetime

print("✅ Database and tables creating.")

DB_NAME = "pitiq.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create probes table
    c.execute('''
        CREATE TABLE IF NOT EXISTS probes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            channel INTEGER NOT NULL,
            created_at TEXT NOT NULL
        );
    ''')

    # Create temperature logs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS temperatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            probe_id INTEGER NOT NULL,
            temperature_c REAL NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (probe_id) REFERENCES probes(id)
        );
    ''')

    conn.commit()
    conn.close()
    print("✅ Database and tables created successfully.")

if __name__ == "__main__":
    init_db()