import pytest
from src.tax_logic import FirmFinantials, TCJAModel

def test_ebitda_regime_limit():
    model = TCJAModel()
    # 2021: 100 EBITDA * 0.3 = 30 limit. D&A shouldn't affect it.
    f = FirmFinantials(year=2021, ebitda=100, depreciation_amortization=40, interest_expense=50)
    assert model.calculate_deduction_limit(f) == 30.0

def test_ebit_regime_limit():
    model = TCJAModel()
    # 2022: (100 EBITDA - 40 D&A) * 0.3 = 18 limit.
    f = FirmFinantials(year=2022, ebitda=100, depreciation_amortization=40, interest_expense=50)
    assert model.calculate_deduction_limit(f) == 18.0

def test_invalid_data():
    # Hardening check: Ensure negative values raise an error
    with pytest.raises(ValueError):
        FirmFinantials(year=2022, ebitda=-100, depreciation_amortization=0, interest_expense=10)
