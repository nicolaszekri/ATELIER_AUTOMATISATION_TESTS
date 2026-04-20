from tester.tests import run_all_tests

def calculate_p95(latencies):
    if not latencies:
        return 0
    latencies = sorted(latencies)
    index = int(0.95 * (len(latencies) - 1))
    return latencies[index]

def execute_test_run():
    tests = run_all_tests()

    passed = sum(1 for t in tests if t["status"] == "PASS")
    failed = sum(1 for t in tests if t["status"] == "FAIL")
    latencies = [t["latency_ms"] for t in tests if "latency_ms" in t]

    latency_avg = round(sum(latencies) / len(latencies), 2) if latencies else 0
    latency_p95 = calculate_p95(latencies)
    error_rate = round(failed / len(tests), 3) if tests else 0

    summary = {
        "passed": passed,
        "failed": failed,
        "error_rate": error_rate,
        "latency_ms_avg": latency_avg,
        "latency_ms_p95": latency_p95
    }

    return {
        "api": "Agify",
        "summary": summary,
        "tests": tests
    }