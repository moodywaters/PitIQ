import sqlite3
import os
from datetime import datetime

DB_NAME = os.path.join(os.path.dirname(__file__), "..", "pitiq.db")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_probes(default_probes):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM probes")
    count = c.fetchone()[0]

    if count == 0:
        print("No probes in DB. Inserting defaults...")
        for probe in default_probes:
            c.execute(
                "INSERT INTO probes (name, channel, created_at) VALUES (?, ?, ?)",
                (probe["name"], probe["channel"], datetime.now().isoformat()),
            )
        conn.commit()
    conn.close()

def get_all_probes():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, channel FROM probes")
    rows = c.fetchall()
    conn.close()
    # Convert to list of dicts for easier use
    return [{"id": r[0], "name": r[1], "channel": r[2]} for r in rows]

def log_temperature(probe_id: int, temperature: float):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        '''
        INSERT INTO temperatures (probe_id, temperature_c, timestamp)
        VALUES (?, ?, ?)
        ''',
        (probe_id, temperature, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    print(f"Logged {temperature}°C for probe {probe_id}")

def get_recent_temperatures(limit=10):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        "SELECT probe_id, temperature_c, timestamp FROM temperatures ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    )
    rows = c.fetchall()
    conn.close()
    return rows
