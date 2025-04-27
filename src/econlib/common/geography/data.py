import functools
from typing import Any, Hashable

import pandas as pd

GEO_STATIC_DATA_BASE_URL = (
    "https://github.com/davidmegginson/ourairports-data/blob/main/"
)


def _get_geo_static_data(file_name: str) -> pd.DataFrame:

    url = f"{GEO_STATIC_DATA_BASE_URL}{file_name}"
    df = pd.read_csv(url)
    return df


@functools.cache
def get_countries() -> list[dict[Hashable, Any]]:
    return _get_geo_static_data("countries.csv").to_dict(orient="records")


@functools.cache
def get_regions() -> list[dict[Hashable, Any]]:
    return _get_geo_static_data("regions.csv").to_dict(orient="records")


@functools.cache
def get_continents() -> list[dict[Hashable, Any]]:
    return [
        {"Code": "AF", "Name": "Africa"},
        {"Code": "AN", "Name": "Antarctica"},
        {"Code": "AS", "Name": "Asia"},
        {"Code": "EU", "Name": "Europe"},
        {"Code": "NA", "Name": "North America"},
        {"Code": "OC", "Name": "Oceania"},
        {"Code": "SA", "Name": "South America"},
    ]
