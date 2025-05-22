from decimal import Decimal

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
        import pdb

        pdb.set_trace()
        return self

    def __next__(self) -> Decimal:
        for _ in range(self.rem_time_units, 0, -1):
            self.current_value += self.current_value * self.setting.rate_change
            return self.current_value
        raise StopIteration("End of time")
