import logging
from typing import ClassVar

import attrs
import tabulate

log = logging.getLogger(__name__)


@attrs.frozen
class Airport:
    """Represents an airport.

    Attributes:
        icao_code: The ICAO code of the airport.
        iata_code: The IATA code of the airport.
        region_code: The region code where the airport is located.
    """

    icao_code: str
    iata_code: str
    region_code: str


@attrs.frozen
class Region:
    """Represents a geographical region.

    Attributes:
        region_code: The code of the region.
        name: The name of the region.
        country_code: The country code where the region is located.
    """

    region_code: str
    name: str
    country_code: str

    _airports_by_code: dict[str, Airport] = attrs.field(
        default=attrs.Factory(dict), init=False
    )

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_airports

        for airport in get_airports():
            if airport["iso_region"] == self.region_code:
                self._airports_by_code[airport["icao_code"]] = Airport(
                    airport["icao_code"],
                    airport["iata_code"],
                    airport["iso_region"],
                )

    def get_airport_count(self) -> int:
        return len(self._airports_by_code)

    def short_summary(self):
        log.info(
            "\nRegion Summary - %s \n\n%s\n",
            self.name,
            tabulate.tabulate(
                [
                    ["Name", self.name],
                    ["Code", self.region_code],
                    ["Number of Airports", len(self._airports_by_code)],
                ],
                headers=["Field", "Value"],
                tablefmt="grid",
            ),
        )


@attrs.frozen
class Country:
    """Represents a country.

    Attributes:
        alpha_2_code: The alpha-2 code of the country.
        name: The name of the country.
        continent_code: The continent code where the country is located.
    """

    alpha_2_code: str
    name: str
    continent_code: str

    _regions_by_code: dict[str, Region] = attrs.field(
        default=attrs.Factory(dict), init=False
    )

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_regions

        for region in get_regions():
            if region["iso_country"] == self.alpha_2_code:
                self._regions_by_code[region["code"]] = Region(
                    region["code"], region["name"], region["iso_country"]
                )

    def get_regions_from_code(self, code) -> Region:
        return self._regions_by_code[code]

    def get_region_count(self) -> int:
        return len(self._regions_by_code)

    def get_airports_count(self) -> int:
        return sum(
            region.get_airport_count() for region in self._regions_by_code.values()
        )

    def short_summary(self):
        log.info(
            "\nCountry Summary - %s \n\n%s\n",
            self.name,
            tabulate.tabulate(
                [
                    ["Name", self.name],
                    ["Code", self.alpha_2_code],
                    ["Number of Regions", len(self._regions_by_code)],
                    ["Number of Airports", self.get_airports_count()],
                ],
                headers=["Field", "Value"],
                tablefmt="grid",
            ),
        )


@attrs.frozen
class Continent:
    """Represents a continent.

    Attributes:
        code: The code of the continent.
        name: The name of the continent.
    """

    code: str
    name: str

    _countries_by_code: dict[str, Country] = attrs.field(
        default=attrs.Factory(dict), init=False
    )

    def __attrs_post_init__(self):
        from econlib.common.geography.data import get_countries

        for country in get_countries():
            if country["continent"] == self.code:
                self._countries_by_code[country["code"]] = Country(
                    country["code"], country["name"], self.code
                )

    def get_country_from_code(self, code) -> Country:
        return self._countries_by_code[code]

    def get_country_count(self) -> int:
        return len(self._countries_by_code)

    def get_airports_count(self) -> int:
        return sum(
            country.get_airports_count() for country in self._countries_by_code.values()
        )

    def short_summary(self):
        log.info(
            "\n\nContinent Summary - %s \n\n%s\n",
            self.name,
            tabulate.tabulate(
                [
                    ["Name", self.name],
                    ["Code", self.code],
                    ["Number of Countries", len(self._countries_by_code)],
                    ["Number of Airports", self.get_airports_count()],
                ],
                headers=["Field", "Value"],
                tablefmt="grid",
            ),
        )


class World:
    """A singleton class representing the world's geographical data.

    This class provides access to continents, countries, regions, and airports.
    It follows the singleton pattern to ensure only one instance of the world's
    data is loaded.
    """

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
    def get_continent_from_code(cls, code) -> Continent:
        return cls._CONTINENTS_BY_CODE[code]

    def get_short_summary_data(self):
        results = [
            [cont.name, cont.get_country_count(), cont.get_airports_count()]
            for cont in self._CONTINENTS_BY_CODE.values()
        ]
        return results

    def short_summary(self):
        log.info(
            "\nWorld Summary \n\n%s\n",
            tabulate.tabulate(
                self.get_short_summary_data(),
                headers=["Continents", "Number of Countries", "Number of Airports"],
                tablefmt="grid",
            ),
        )
