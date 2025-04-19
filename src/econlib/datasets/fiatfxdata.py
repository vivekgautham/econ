import datetime

import httpx
from dateutil.rrule import DAILY, rrule


class EndpointFactory:

    BASE_URL = "https://api.exchangeratesapi.io/v1/"
    API_KEY = "17c2b9fd0b3746fbbe13f0b0479a4bbf"

    @classmethod
    def get_historical_rates_endpoint(cls, date):
        """Get Historical End points"""
        return f"{cls.BASE_URL}{date.strftime("%Y-%m-%d")}?access_key={cls.API_KEY}"


def get_historical_fiatfx_data():
    dates = rrule(DAILY, dtstart=datetime.date.today(), until=datetime.date.today())
    base_ccy = None
    historical_data = []
    for cur_day in dates:
        response = httpx.get(
            EndpointFactory.get_historical_rates_endpoint(cur_day),
            timeout=None,
        )
        data = response.json()
        for ccy, rate in data["rates"].items():
            base_ccy = data["base"]
            historical_data.append(
                {
                    "date": cur_day.strftime("%Y%m%d"),
                    "base_ccy": data["base"],
                    "quote_ccy": ccy,
                    "rate": rate,
                }
            )

    historical_df = pd.DataFrame(historical_data)
    historical_df = historical_df[
        (historical_df.quote_ccy.isin(to_ccys.split(",")))
    ].copy(deep=True)
