from typing import ClassVar

import attrs


@attrs.frozen
class Region:
    region_code: str
    name: str
    country_code: str


@attrs.frozen
class Country:
    alpha_2_code: str
    alpha_3_code: str
    numeric_code: str
    name: str
    continent_code: str
    regions: tuple[Region]


@attrs.frozen
class Continent:
    code: str
    name: str
    countries: tuple[Country]


class World:
    """World Geo Api"""

    _CONTINENTS_BY_CODE: ClassVar[dict[str, Continent]] = {}
    _COUNTRIES_BY_CODE: ClassVar[dict[str, Continent]] = {}

    @classmethod
    def get_continent_from_code(cls, code):
        pass

    @classmethod
    def get_country_from_code(cls, code):
        pass
