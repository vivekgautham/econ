from decimal import Decimal
from enum import Enum

import attrs


class IntervalUnit(Enum):
    """Represents the time interval for calculations."""

    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"


@attrs.define
class InputParams:
    """Represents the input parameters for a financial calculation.

    Attributes:
        amount: The initial principal amount.
        rate_schedule: A dictionary mapping sequence IDs to interest rates.
        withdrawal_schedule: A dictionary mapping sequence IDs to withdrawal amounts.
        interval_unit: The time interval for the calculation.
    """

    amount: Decimal
    rate_schedule: dict[int, Decimal]
    withdrawal_schedule: dict[int, Decimal]
    interval_unit: IntervalUnit


@attrs.define
class CashFlowOutput:
    """Represents the output of a single cash flow interval.

    Attributes:
        sequence_id: The sequence number of the interval.
        interval_period: A string representing the time period of the interval.
        amount: The total amount at the end of the interval.
        principal_in: The principal amount at the beginning of the interval.
        interest_earned: The interest earned during the interval.
    """

    sequence_id: int
    interval_period: str
    amount: Decimal
    principal_in: Decimal
    interest_earned: Decimal
