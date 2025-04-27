import functools

import pandas as pd

GEO_STATIC_DATA_BASE_URL = (
    "https://github.com/davidmegginson/ourairports-data/blob/main/"
)


@functools.cache
def get_countries():
    countries_file = "countries.csv"
    url = f"{GEO_STATIC_DATA_BASE_URL}{countries_file}"
    df = pd.read_csv(url)
    return df


@functools.cache
def get_regions():
    countries_file = "countries.csv"
    url = f"{GEO_STATIC_DATA_BASE_URL}{countries_file}"
    df = pd.read_csv(url)
    return df
