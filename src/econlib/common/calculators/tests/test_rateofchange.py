from decimal import Decimal

from econlib.common.calculators import rateofchange


def test_change_calculator():
    setting = rateofchange.Setting(Decimal(3.9), 7, Decimal(0.07))
    change_calc = rateofchange.ChangeCalculator(setting)
    assert list(change_calc) == (
        [
            Decimal("4.172999999999999930944127868"),
            Decimal("4.465109999999999953907980909"),
            Decimal("4.777667699999999980425147150"),
            Decimal("5.112104439000000010880567558"),
            Decimal("5.469951749730000045695663602"),
            Decimal("5.852848372211100085331558311"),
            Decimal("6.262547758265877130292569528"),
            Decimal("6.700926101344488571129997679"),
        ]
    )
