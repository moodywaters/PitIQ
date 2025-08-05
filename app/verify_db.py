import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "..", "pitiq.db")

def verify_db():
    print(f"Using database at: {os.path.abspath(DB_NAME)}\n")

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Show all probes
    print("=== Probes Table ===")
    c.execute("SELECT id, name, channel, created_at FROM probes")
    probes = c.fetchall()
    if probes:
        for p in probes:
            print(f"ID: {p[0]} | Name: {p[1]} | Channel: {p[2]} | Created: {p[3]}")
    else:
        print("No probes found.")
    print()

    # Show last 10 temperature readings
    print("=== Last 10 Temperature Logs ===")
    c.execute("""
        SELECT t.id, p.name, t.temperature_c, t.timestamp
        FROM temperatures t
        JOIN probes p ON t.probe_id = p.id
        ORDER BY t.timestamp DESC
        LIMIT 10
    """)
    temps = c.fetchall()
    if temps:
        for t in temps:
            print(f"LogID: {t[0]} | Probe: {t[1]} | Temp: {t[2]}°C | Time: {t[3]}")
    else:
        print("No temperature logs found.")

    conn.close()

if __name__ == "__main__":
    verify_db()
