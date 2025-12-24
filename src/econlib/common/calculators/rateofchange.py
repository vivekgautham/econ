from decimal import Decimal

import attrs


@attrs.define
class Setting:
    """Represents the settings for a change calculation.

    Attributes:
        initial_value: The starting value for the calculation.
        time_units: The number of time units over which the calculation will occur.
        rate_change: The rate of change per time unit.
    """

    initial_value: Decimal
    time_units: int
    rate_change: Decimal


class ChangeCalculator:
    """An iterator that calculates a value changing over time.

    The calculator takes a `Setting` object and computes the new value
    for each time unit based on the provided rate of change.

    Attributes:
        setting: The `Setting` object for the calculation.
        current_value: The current value in the iteration.
        rem_time_units: The remaining time units in the iteration.
    """

    def __init__(self, setting: Setting) -> None:
        self.setting = setting
        self.current_value = setting.initial_value
        self.rem_time_units = setting.time_units

    def __iter__(self):
        return self

    def __next__(self) -> Decimal:
        if self.rem_time_units == 0:
            raise StopIteration("End of time")

        self.current_value += self.current_value * self.setting.rate_change
        self.rem_time_units -= 1
        return self.current_value
