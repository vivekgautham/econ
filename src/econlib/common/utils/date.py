import math
from datetime import datetime


def get_current_utc_datetime() -> datetime:
    """
    Returns the current datetime in UTC.
    """
    return datetime.now(datetime.timezone.utc)


def get_year_month_format(date_obj: datetime) -> str:
    """
    Accepts a datetime object and returns a string in 'YYYYMM' format.
    """
    return date_obj.strftime("%Y%m")


def get_year_quarter_format(date_obj: datetime) -> str:
    """
    Accepts a datetime object and returns a string in 'YYYYQQQ' format.
    """
    year = date_obj.year
    quarter = math.ceil(date_obj.month / 3)
    return f"{year}Q{quarter}"
