import pytest

from econlib.programs.aliendictionary import alienOrder


@pytest.mark.parametrize(
    ("input_list", "expected"),
    [(["wrt", "wrf", "er", "ett", "rftt"], "wertf"), (["z", "x"], "zx")],
)
def test_aliendictionary(input_list, expected):
    assert expected == alienOrder(input_list)
