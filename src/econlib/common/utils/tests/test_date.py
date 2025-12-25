from datetime import datetime

import pytest

from econlib.common.utils.date import (get_year_month_format,
                                       get_year_quarter_format)


@pytest.mark.parametrize(
    "date_obj, expected_format",
    [
        (datetime(2023, 1, 1), "202301"),
        (datetime(2024, 12, 31), "202412"),
        (datetime(2020, 5, 15), "202005"),
    ],
)
def test_get_year_month_format(date_obj, expected_format):
    """
    Test that get_year_month_format returns the date in 'YYYYMM' format.
    """
    assert get_year_month_format(date_obj) == expected_format


@pytest.mark.parametrize(
    "date_obj, expected_format",
    [
        (datetime(2023, 1, 1), "2023Q1"),
        (datetime(2023, 3, 31), "2023Q1"),
        (datetime(2023, 4, 1), "2023Q2"),
        (datetime(2023, 6, 30), "2023Q2"),
        (datetime(2023, 7, 1), "2023Q3"),
        (datetime(2023, 9, 30), "2023Q3"),
        (datetime(2023, 10, 1), "2023Q4"),
        (datetime(2023, 12, 31), "2023Q4"),
        (datetime(2024, 2, 15), "2024Q1"),
    ],
)
def test_get_year_quarter_format(date_obj, expected_format):
    """
    Test that get_year_quarter_format returns the date in 'YYYYQQQ' format.
    """
    assert get_year_quarter_format(date_obj) == expected_format
