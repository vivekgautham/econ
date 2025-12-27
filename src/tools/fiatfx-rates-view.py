#!/usr/local/bin/economics/bin/python
import argparse

from econlib.datasets.fx.primary import get_primary_fiat_fx_stats


def run_rates_view(args):
    """Run Rates View per arguments"""
    get_primary_fiat_fx_stats(args.base_currency, args.quote_currency)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fiat FX view")
    view = parser.add_argument_group("fx ccy")
    view.add_argument(
        "-base", "--base_currency", help="base currency symbol", required=True
    )
    view.add_argument(
        "-quote", "--quote_currency", help="quote currency symbol", required=True
    )

    args = parser.parse_args()

    run_rates_view(args)
