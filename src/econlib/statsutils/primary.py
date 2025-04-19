import logging
import httpx
from econlib.datasets import fiatfxdata
import tabulate
from datetime import datetime
from dateutil.rrule import rrule, DAILY
import pandas as pd

log = logging.getLogger(__name__) 

def get_primary_stats(start_date, end_date, base_ccy, to_ccy):
    log.info("Running Primary Stats for Fiat %s", to_ccy)
    dates = rrule(DAILY, dtstart=start_date, until=end_date)
    historical_data = []
    for date in dates:
        response = httpx.get(fiatfxdata.EndpointFactory.get_historical_rates_endpoint(date, base_ccy, [to_ccy]), timeout=None)
        data = response.json()
        for ccy, rate in data["rates"]:
            historical_data.append({"date": date, "ccy": ccy, "rate": rate})

    historical_df = pd.DataFrame(historical_data)
    import pdb 
    pdb.set_trace()
    _ = 2

    