import logging
import httpx
from econlib.datasets import fiatfxdata
import tabulate
from datetime import datetime, date
from dateutil.rrule import rrule, DAILY
import pandas as pd


log = logging.getLogger(__name__)


def get_primary_stats(from_ccy, to_ccys):
    log.info("Running Primary Stats for Fiat FXs %s", to_ccys)
    dates = rrule(DAILY, dtstart=date.today(), until=date.today())
    base_ccy = None
    historical_data = []
    for cur_day in dates:
        response = httpx.get(
            fiatfxdata.EndpointFactory.get_historical_rates_endpoint(cur_day),
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

    pivot_view = pd.DataFrame(
        historical_df.pivot(index="quote_ccy", columns="date", values="rate")
        .reset_index()
        .to_dict(orient="records")
    )

    log.info(
        "Rates Against %s \n %s",
        base_ccy,
        tabulate.tabulate(
            pivot_view.values.tolist(), headers=pivot_view.columns, tablefmt="grid"
        ),
    )
    return pivot_view
