import requests
import time

def make_request(url, timeout=3, retries=1):
    last_error = None

    for _ in range(retries + 1):
        try:
            start = time.time()
            response = requests.get(url, timeout=timeout)
            latency_ms = round((time.time() - start) * 1000, 2)
            return response, latency_ms
        except requests.RequestException as e:
            last_error = str(e)

    return None, last_error