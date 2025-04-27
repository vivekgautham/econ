#!/usr/local/bin/economics/bin/python
import argparse

from econlib.common.geography.data import World


def world_view(args):
    """Run Rates View per arguments"""
    world = World()

    world.get_


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="World view")

    view = parser.add_argument_group("continent")
    view.add_argument("--c", "--continent-code", help="continent code", required=True)

    args = parser.parse_args()

    world_view(args)
