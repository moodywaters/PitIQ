import random
import time
import os
from app.db import init_probes, log_temperature, get_all_probes

DEFAULT_PROBES = [
    {"name": "Smoker", "channel": 0},
    {"name": "Brisket", "channel": 1},
    {"name": "Chicken", "channel": 2},
    {"name": "Spare Probe", "channel": 3},
]

def read_probe_temperature(probe_name: str) -> float:
    if probe_name.lower() == "smoker":
        return round(random.uniform(95, 125), 1)
    else:
        return round(random.uniform(20, 95), 1)

def simulate_and_log(iterations: int = 5, delay: int = 2):
    # Log the absolute path of the DB
    from db import DB_NAME
    print(f"Using database at: {os.path.abspath(DB_NAME)}")

    # Ensure probes exist
    init_probes(DEFAULT_PROBES)

    # Fetch probes with correct DB IDs
    probes = get_all_probes()
    print(f"Active probes from DB: {probes}\n")

    for i in range(iterations):
        print(f"--- Reading {i+1} ---")
        for probe in probes:
            temp = read_probe_temperature(probe["name"])
            print(f"Generated temp for {probe['name']} (ID {probe['id']}): {temp}°C")

            # Attempt DB insert
            try:
                log_temperature(probe["id"], temp)
                print(f"✅ Logged {temp}°C for probe {probe['name']} (ID {probe['id']})")
            except Exception as e:
                print(f"❌ Failed to log {probe['name']} (ID {probe['id']}) - {e}")

        print("Iteration complete.\n")
        time.sleep(delay)

if __name__ == "__main__":
    simulate_and_log()
