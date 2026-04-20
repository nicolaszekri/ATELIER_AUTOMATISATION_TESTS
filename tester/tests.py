from tester.client import make_request

BASE_URL = "https://api.agify.io"

def test_status_code():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response and response.status_code == 200:
        return {"name": "Status code 200", "status": "PASS", "latency_ms": latency}
    return {"name": "Status code 200", "status": "FAIL", "details": "Code différent de 200"}

def test_json_content_type():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response and "application/json" in response.headers.get("Content-Type", ""):
        return {"name": "Content-Type JSON", "status": "PASS", "latency_ms": latency}
    return {"name": "Content-Type JSON", "status": "FAIL", "details": "Pas du JSON"}

def test_field_name_exists():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response:
        data = response.json()
        if "name" in data:
            return {"name": "Champ name présent", "status": "PASS", "latency_ms": latency}
    return {"name": "Champ name présent", "status": "FAIL", "details": "Champ absent"}

def test_field_age_exists():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response:
        data = response.json()
        if "age" in data:
            return {"name": "Champ age présent", "status": "PASS", "latency_ms": latency}
    return {"name": "Champ age présent", "status": "FAIL", "details": "Champ absent"}

def test_field_count_exists():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response:
        data = response.json()
        if "count" in data:
            return {"name": "Champ count présent", "status": "PASS", "latency_ms": latency}
    return {"name": "Champ count présent", "status": "FAIL", "details": "Champ absent"}

def test_name_type_string():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response:
        data = response.json()
        if isinstance(data.get("name"), str):
            return {"name": "Type de name = string", "status": "PASS", "latency_ms": latency}
    return {"name": "Type de name = string", "status": "FAIL", "details": "Type incorrect"}

def test_latency_under_3000ms():
    response, latency = make_request(f"{BASE_URL}?name=michael")
    if response and latency < 3000:
        return {"name": "Latence < 3000 ms", "status": "PASS", "latency_ms": latency}
    return {"name": "Latence < 3000 ms", "status": "FAIL", "details": "Latence trop élevée"}

def run_all_tests():
    return [
        test_status_code(),
        test_json_content_type(),
        test_field_name_exists(),
        test_field_age_exists(),
        test_field_count_exists(),
        test_name_type_string(),
        test_latency_under_3000ms()
    ]