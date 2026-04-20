import sqlite3
import json
from datetime import datetime

DB_NAME = "runs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            api_name TEXT NOT NULL,
            passed INTEGER NOT NULL,
            failed INTEGER NOT NULL,
            error_rate REAL NOT NULL,
            latency_avg REAL NOT NULL,
            latency_p95 REAL NOT NULL,
            details TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_run(api_name, summary, tests):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO runs (
            timestamp, api_name, passed, failed, error_rate,
            latency_avg, latency_p95, details
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        api_name,
        summary["passed"],
        summary["failed"],
        summary["error_rate"],
        summary["latency_ms_avg"],
        summary["latency_ms_p95"],
        json.dumps(tests)
    ))
    conn.commit()
    conn.close()

def list_runs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, timestamp, api_name, passed, failed, error_rate,
               latency_avg, latency_p95, details
        FROM runs
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows