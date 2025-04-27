#!/usr/local/bin/economics/bin/python

from econlib.datasets.fred import fetch_spot_rates


def show_spot_rates():
    """Show Spot Rates"""
    fetch_spot_rates()


if __name__ == "__main__":
    show_spot_rates()
