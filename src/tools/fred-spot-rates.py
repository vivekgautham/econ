#!/usr/local/bin/economics/bin/python
import datetime

from rich.prompt import Prompt

from econlib.datasets.fred.connect import fetch_spot_rates


def show_spot_rates(start_date: datetime.date, end_date: datetime.date):
    """Show Spot Rates"""
    fetch_spot_rates(datetime.date(2025, 4, 13), datetime.date(2025, 4, 18))


if __name__ == "__main__":
    start_date_response = Prompt.ask("Enter Start Date (YYYYMMDD): ")
    end_date_response = Prompt.ask("Enter End Date (YYYYMMDD): ")
    print(start_date_response, end_date_response)
    show_spot_rates(
        datetime.datetime.strptime(start_date_response.strip(), "%Y%m%d").date(),
        datetime.datetime.strptime(start_date_response.strip(), "%Y%m%d").date(),
    )
