#!/usr/local/bin/economics/bin/python
import datetime

from econlib.datasets.fred.connect import fetch_spot_rates


def show_spot_rates():
    """Show Spot Rates"""
    fetch_spot_rates(datetime.date(2025, 4, 1), datetime.date(2025, 4, 18))


if __name__ == "__main__":
    show_spot_rates()
