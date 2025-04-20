import pytest

from econlib.programs.strobogrammatic import strobogrammaticInRange


@pytest.mark.parametrize(
    ("low", "high", "expected"),
    [
        ("50", "100", 3),
        ("150", "200", 1),
    ],
)
def test_strobogrammaticInRange(low, high, expected):
    assert expected == strobogrammaticInRange(low, high)
