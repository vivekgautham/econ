from decimal import Decimal

from econlib.common.calculators import rateofchange


def test_change_calculator():
    setting = rateofchange.Setting(Decimal(3.9), 7, 7)
    change_calc = rateofchange.ChangeCalculator(setting)
    assert list(change_calc) == []
