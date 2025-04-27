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

    _REGIONS_BY_CODE: ClassVar[dict[str, Region]] = {}

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_regions

        for continent in get_regions():
            self._REGIONS_BY_CODE[continent["Code"]] = Region(
                continent["Code"], continent["Name"]
            )


@attrs.frozen
class Continent:
    code: str
    name: str

    _COUNTRIES_BY_CODE: ClassVar[dict[str, Country]] = {}

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_countries

        for country in get_countries():
            self._COUNTRIES_BY_CODE[country["code"]] = Country(
                country["code"], country["name"]
            )

    def short_summary(self):
        log.info("%s", self.name)
        tabulate.tabulate(
            [["Name", self.name], ["Code", self.code]],
            headers=["Field", "Value"],
            tablefmt="grid",
        ),


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
        pass

    @classmethod
    def get_country_from_code(cls, code):
        pass
