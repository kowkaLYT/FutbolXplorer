import requests

API_KEY = "c4998ba00908904056dca85a90b1b28d"
BASE_URL = "https://v3.football.api-sports.io"


def make_request(endpoint, params):
    url = f"{BASE_URL}/{endpoint}"
    headers = {"x-apisports-key": API_KEY, "Content-Type": "application/json"}

    print(f"\nЗапит до API: {url} з параметрами {params}")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("response") or None

    print(f"Помилка {response.status_code}: {response.text}")
    return None
