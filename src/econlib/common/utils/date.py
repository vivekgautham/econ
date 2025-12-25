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
