from fastapi import FastAPI
from app.db import get_recent_temperatures, get_all_probes
from fastapi.responses import JSONResponse

app = FastAPI(title="PitIQ Temperature Monitor")

@app.get("/")
def root():
    return {"message": "Welcome to PitIQ - BBQ Temperature Monitor"}

@app.get("/probes")
def list_probes():
    return get_all_probes()

@app.get("/latest")
def latest_readings(limit: int = 5):
    """Return the latest temperature readings"""
    rows = get_recent_temperatures(limit)
    data = [
        {"probe_id": r[0], "temperature_c": r[1], "timestamp": r[2]}
        for r in rows
    ]
    return JSONResponse(content=data)
