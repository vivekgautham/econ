import grequests

API_KEY = "2d9fe8dbad89dabfd5afba8ca6e5f4f6"

FRED_URL = f"https://api.stlouisfed.org/fred/series/observations?api_key={API_KEY}"


SERIES_NAMES = [
    "DEXINUS",
    "DEXCHUS",
    "DEXJPUS",
    "DEXUSUK",
]


URLS = [f"{FRED_URL}&series_id={series}&file_type=json" for series in SERIES_NAMES]


def write_to_file(response):
    json_data = response.json()


def fetch_spot_rates():
    tasks = []
    for url in URLS:
        action_item = grequests.get(url, hooks={"response": write_to_file})
        tasks.append(action_item)
    grequests.map(tasks)
