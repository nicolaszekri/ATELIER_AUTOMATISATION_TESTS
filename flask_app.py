from flask import Flask, jsonify, render_template
from storage import init_db, save_run, list_runs
from tester.runner import execute_test_run
import json

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return "API Monitoring App OK"

@app.route("/run")
def run_tests():
    result = execute_test_run()
    save_run(result["api"], result["summary"], result["tests"])
    return jsonify(result)

@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    formatted_runs = []

    for run in runs:
        formatted_runs.append({
            "id": run[0],
            "timestamp": run[1],
            "api_name": run[2],
            "passed": run[3],
            "failed": run[4],
            "error_rate": run[5],
            "latency_avg": run[6],
            "latency_p95": run[7],
            "details": json.loads(run[8])
        })

    return render_template("dashboard.html", runs=formatted_runs)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})