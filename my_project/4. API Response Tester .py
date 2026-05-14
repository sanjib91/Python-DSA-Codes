# Problem: Test API responses and report failures
def test_api_endpoints(endpoints):
    import requests
    from datetime import datetime

    results = []

    for url in endpoints:
        try:
            response = requests.get(url, timeout=5)
            status = "PASS" if response.status_code == 200 else f"FAIL({response.status.code})"

        except Exception as e:
            status = f"ERROR ({str(e)})"

    results.append({
        'url': url,
        'status': status,
        'timestamp': datetime.now().isoformat()
    })

    return results

# Test with mock data
endpoints = ["https://api.example.com/users", "https://api.example.com/products"]
print(test_api_endpoints(endpoints))