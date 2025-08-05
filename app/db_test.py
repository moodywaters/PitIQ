import sqlite3
from datetime import datetime

DB_NAME = "pitiq.db"

def test_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # 1. Insert a dummy probe
    c.execute('''
        INSERT INTO probes (name, channel, created_at)
        VALUES (?, ?, ?)
    ''', ("Test Probe", 1, datetime.now().isoformat()))

    probe_id = c.lastrowid
    print(f"Inserted dummy probe with ID: {probe_id}")

    # 2. Insert a dummy temperature reading
    c.execute('''
        INSERT INTO temperatures (probe_id, temperature_c, timestamp)
        VALUES (?, ?, ?)
    ''', (probe_id, 123.45, datetime.now().isoformat()))
    conn.commit()

    # 3. Read back data to verify
    c.execute('SELECT * FROM probes')
    print("Probes in DB:", c.fetchall())

    c.execute('SELECT * FROM temperatures')
    print("Temperatures in DB:", c.fetchall())

    conn.close()
    print("✅ Database verification complete!")

if __name__ == "__main__":
    test_db()
