import functools

import pandas as pd

GEO_STATIC_DATA_BASE_URL = (
    "https://github.com/davidmegginson/ourairports-data/blob/main/"
)


def _get_geo_static_data(file_name: str) -> pd.DataFrame:

    url = f"{GEO_STATIC_DATA_BASE_URL}{file_name}"
    df = pd.read_csv(url)
    return df


@functools.cache
def get_countries():
    return _get_geo_static_data("countries.csv")


@functools.cache
def get_regions():
    return _get_geo_static_data("regions.csv")
