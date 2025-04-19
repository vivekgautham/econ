import logging
import httpx
from econlib.datasets import fiatfxdata
import tabulate

log = logging.getLogger(__name__) 

def get_primary_stats(base_ccy, to_ccy):
    log.info("Running Primary Stats for Fiat %s", to_ccy)
    data = httpx.get(f"{fiatfxdata.API_KEY}&base={base_ccy}&symbols={to_ccy}").json()

    