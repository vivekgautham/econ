from decimal import Decimal
from enum import Enum

import attrs


class IntervalUnit(Enum):
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"


@attrs.define
class InputParams:
    amount: Decimal
    rate_schedule: dict[int, Decimal]
    withdrawal_schedule: dict[int, Decimal]
    interval_unit: IntervalUnit


@attrs.define
class CashFlowOutput:
    sequence_id: int
    interval_period: str
    amount: Decimal
    principal_in: Decimal
    interest_earned: Decimal
