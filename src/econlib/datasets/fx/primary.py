"""
Provides functions for retrieving and processing primary fiat foreign exchange (FX) rate statistics.
"""

import logging
import time

import pandas as pd
import tabulate

from econlib.datasets.fx import fiatfxdata

log = logging.getLogger(__name__)


def get_primary_fiat_fx_stats(from_ccy: str, to_ccy: str) -> pd.DataFrame:
    """
    Retrieves and processes primary fiat foreign exchange (FX) rate statistics
    between a base currency and a quote currency.

    Args:
        from_ccy (str): The base currency code (e.g., "USD").
        to_ccy (str): The quote currency code (e.g., "EUR").

    Returns:
        pd.DataFrame: A DataFrame containing the pivoted FX rates, with the base currency
                      as the index and dates as columns.
    """
    log.info("Running Primary Stats for Fiat FXs %s", to_ccy)
    historical_df_to_ccy = fiatfxdata.get_historical_fiatfx_data(to_ccy)
    log.info("Sleeping for 10 secs")
    time.sleep(10)
    historical_df_base_ccy = fiatfxdata.get_historical_fiatfx_data(from_ccy)
    final_df = historical_df_base_ccy.merge(historical_df_to_ccy, on=["date"])
    final_df["quote_ccy"] = to_ccy
    final_df["rate"] = final_df["rate_y"] / final_df["rate_x"]
    pivot_view = pd.DataFrame(
        final_df.pivot(index="quote_ccy", columns="date", values="rate")
        .reset_index()
        .rename(columns={"quote_ccy": from_ccy})
        .to_dict(orient="records")
    )
    log.info(
        "Rates Against %s \n %s",
        from_ccy,
        tabulate.tabulate(
            pivot_view.values.tolist(), headers=pivot_view.columns, tablefmt="grid"
        ),
    )
    return pivot_view
