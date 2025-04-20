from decimal import Decimal
from enum import Enum
from typing import TypeVar

import attrs

T = TypeVar("T")


class IntervalUnit(Enum):
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"


@attrs.define
class AmountAtRate:
    amount: Decimal
    rate: Decimal
    withdrawal_schedule: list[Decimal]
    total_interval_units: int
    interval_unit: IntervalUnit


@attrs.define
class CompoundingCashFlowUnit:
    sequence_id: int
    interval_period: str
    amount: Decimal
    principal_in: Decimal
    interest_earned: Decimal
