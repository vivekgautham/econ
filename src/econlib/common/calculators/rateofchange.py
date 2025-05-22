from decimal import Decimal
from typing import Generator

import attrs


@attrs.define
class Setting:
    initial_value: Decimal
    time_units: int
    rate_change: Decimal


class ChangeCalculator:

    def __init__(self, setting: Setting) -> None:
        self.setting = setting
        self.current_value = setting.initial_value
        self.rem_time_units = setting.time_units

    def __iter__(self):
        return self

    def __next__(self) -> Generator[Decimal]:
        if self.rem_time_units > 0:
            self.current_value += self.current_value * self.setting.rate_change
            self.rem_time_units -= 1
            yield self.current_value
