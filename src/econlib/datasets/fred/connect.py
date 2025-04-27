import datetime
import logging

import grequests
import pandas as pd
import tabulate

from econlib.common.perf.timeit import timeit

log = logging.getLogger(__name__)

API_KEY = "2d9fe8dbad89dabfd5afba8ca6e5f4f6"

FRED_URL = f"https://api.stlouisfed.org/fred/series/observations?api_key={API_KEY}"


SERIES_NAMES = [
    "DEXINUS",
    "DEXCHUS",
    "DEXJPUS",
    "DEXUSUK",
    "DEXUSAL",
    "DEXCAUS",
    "DEXKOUS",
    "DEXUSEU",
]


URLS = [f"{FRED_URL}&series_id={series}&file_type=json" for series in SERIES_NAMES]


@timeit
def fetch_spot_rates(start_date: datetime.date, end_date: datetime.date):
    tasks = []
    for url in URLS:
        action_item = grequests.get(url)
        tasks.append(action_item)
    responses = grequests.map(tasks)
    data = []
    for series_name, response in zip(SERIES_NAMES, responses):
        json_data = response.json()
        observations = json_data["observations"]
        for row in observations:
            data.append(
                {
                    "Series": series_name,
                    "Rate": row["value"],
                    "Date": datetime.datetime.strptime(row["date"], "%Y-%m-%d").date(),
                }
            )

    rates_df = pd.DataFrame(data)
    filtered_rates_df = (
        rates_df[(rates_df.Date >= start_date) & (rates_df.Date <= end_date)]
        .pivot(index="Series", columns="Date", values="Rate")
        .reset_index()
    )
    log.info(
        "\nRates\n%s",
        tabulate.tabulate(
            filtered_rates_df.values.tolist(),
            headers=filtered_rates_df.columns,
            tablefmt="fancy_grid",
            numalign="right",
            stralign="left",
        ),
    )
    return data
