#!/usr/local/bin/economics/bin/python
import argparse

from econlib.common.geography.models import World


def region_view(country, args):
    if args.rgc:
        region = country.get_regions_from_code(args.rgc)
        region.short_summary()
    else:
        country.short_summary()


def country_view(continent, args):
    if args.ctc:
        country = continent.get_country_from_code(args.ctc)
        region_view(country, args)
    else:
        continent.short_summary()


def continent_view(world, args):
    if args.coc:
        continent = world.get_continent_from_code(args.coc)
        country_view(continent, args)
    else:
        world.short_summary()


def world_view(args):
    """Run World View per arguments"""
    world = World()
    continent_view(world, args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="World view")

    parser.add_argument("-coc", "-continentcode", help="continent code", required=False)
    parser.add_argument("-ctc", "-countrycode", help="country code", required=False)
    parser.add_argument("-rgc", "-regioncode", help="region code", required=False)

    args = parser.parse_args()

    world_view(args)
