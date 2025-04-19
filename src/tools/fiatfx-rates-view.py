#!/usr/local/bin/economics/bin/python
import argparse

from econlib.statsutils.primary import get_primary_stats
from econlib.statsutils.views import View


def run_rates_view(args):

    view_map = {
        View.PRIMARY.value: get_primary_stats
    }

    view_map[args.view](args.currency)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fiat FX view')

    view = parser.add_argument_group('name of fx view')
    view.add_argument('-v', '--view', help='view name', required=True, choices=[v.value for v in View])
    view.add_argument('-ccy', '--currency', help='currency symbol', required=True)

    args = parser.parse_args()

    if args.view:
        run_rates_view(args)
