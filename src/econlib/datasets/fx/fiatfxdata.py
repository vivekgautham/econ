import datetime

import httpx
import pandas as pd
from dateutil.rrule import DAILY, rrule


class EndpointFactory:
    """A factory for creating exchangeratesapi.io API endpoints."""

    BASE_URL = "https://api.exchangeratesapi.io/v1/"
    API_KEY = "17c2b9fd0b3746fbbe13f0b0479a4bbf"

    @classmethod
    def get_historical_rates_endpoint(cls, date):
        """Get Historical End points"""
        return f"{cls.BASE_URL}{date.strftime("%Y-%m-%d")}?access_key={cls.API_KEY}"


def get_historical_fiatfx_data(to_ccys: list[str]) -> pd.DataFrame:
    dates = rrule(DAILY, dtstart=datetime.date.today(), until=datetime.date.today())
    base_ccy = None
    historical_data = []
    all_ccys_available = set()
    ccy_pairs = {}
    for cur_day in dates:
        response = httpx.get(
            EndpointFactory.get_historical_rates_endpoint(cur_day),
            timeout=None,
        )
        data = response.json()
        base_ccy = data["base"]
        all_ccys_available.add(base_ccy)
        for ccy, rate in data["rates"].items():
            historical_data.append(
                {
                    "date": cur_day.strftime("%Y%m%d"),
                    "base_ccy": data["base"],
                    "quote_ccy": ccy,
                    "rate": rate,
                }
            )
            ccy_pairs[(base_ccy, ccy)] = rate
            all_ccys_available.add(ccy)

    historical_df = pd.DataFrame(historical_data)
    historical_df = historical_df[
        (historical_df.quote_ccy.isin(to_ccys.split(",")))
    ].copy(deep=True)
    return historical_df
