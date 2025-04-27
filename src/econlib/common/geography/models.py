import logging
from typing import ClassVar

import attrs
import tabulate

log = logging.getLogger(__name__)


@attrs.frozen
class Region:
    region_code: str
    name: str
    country_code: str


@attrs.frozen
class Country:
    alpha_2_code: str
    name: str
    continent_code: str

    _regions_by_code: dict[str, Region] = attrs.field(default={}, init=False)

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_regions

        for region in get_regions():
            if region["iso_country"] == self.alpha_2_code:
                self._regions_by_code[region["code"]] = Region(
                    region["code"], region["name"], region["iso_country"]
                )


@attrs.frozen
class Continent:
    code: str
    name: str

    _countries_by_code: dict[str, Country] = attrs.field(default={}, init=False)

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_countries

        for country in get_countries():
            if country["continent"] == self.code:
                self._countries_by_code[country["code"]] = Country(
                    country["code"], country["name"], self.code
                )

    def short_summary(self):
        log.info(
            "\n\nContinent Summary - %s \n\n%s\n",
            self.name,
            tabulate.tabulate(
                [["Name", self.name], ["Code", self.code]],
                headers=["Field", "Value"],
                tablefmt="grid",
            ),
        )


class World:
    """World Geo Api"""

    _CONTINENTS_BY_CODE: ClassVar[dict[str, Continent]] = {}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(World, cls).__new__(cls)
            cls.setup()
        return cls.instance

    @classmethod
    def setup(cls):
        from econlib.common.geography.data import get_continents

        for continent in get_continents():
            cls._CONTINENTS_BY_CODE[continent["Code"]] = Continent(
                continent["Code"], continent["Name"]
            )

    @classmethod
    def get_continent_from_code(cls, code):
        return cls._CONTINENTS_BY_CODE[code]

    @classmethod
    def get_country_from_code(cls, code):
        pass
