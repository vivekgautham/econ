#!/usr/local/bin/economics/bin/python
"""World view.

A command-line tool to view information about continents, countries, and regions.
"""
import argparse

from econlib.common.geography.models import World


def view(world: World, args: argparse.Namespace) -> None:
    """View the world

    Args:
        entity: The entity to view.
        args: The command-line arguments.
    """
    if args.continent:
        continent = world.get_continent_from_code(args.continent)
        if args.country:
            country = continent.get_country_from_code(args.country)
            if args.region:
                region = country.get_regions_from_code(args.region)
                region.short_summary()
            else:
                country.short_summary()
        else:
            continent.short_summary()
    else:
        world.short_summary()


def main():
    """Run the world view script."""
    parser = argparse.ArgumentParser(
        description="A command-line tool to view information about continents, countries, and regions."
    )

    parser.add_argument(
        "--continent", help="The code of the continent to view.", required=False
    )
    parser.add_argument(
        "--country", help="The code of the country to view.", required=False
    )
    parser.add_argument(
        "--region", help="The code of the region to view.", required=False
    )

    args = parser.parse_args()

    world = World()
    view(world, args)


if __name__ == "__main__":
    main()
