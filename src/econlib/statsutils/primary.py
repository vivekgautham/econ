import logging
from datetime import date, datetime

import httpx
import pandas as pd
import tabulate

from econlib.datasets import fiatfxdata

log = logging.getLogger(__name__)


def get_primary_fiat_fx_stats(from_ccy, to_ccys):
    log.info("Running Primary Stats for Fiat FXs %s", to_ccys)
    base_ccy, historical_df = fiatfxdata.get_historical_fiatfx_data(to_ccys)
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
