from decimal import Decimal
from enum import Enum


class IntervalUnit(Enum):
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"


class AmountAtRate:
    amount: Decimal
    rate: Decimal
    interval: Decimal
    interval_unit: IntervalUnit


def get_cag():
    pass
