import pytest
# Ensure the import matches the exact class names in src/tax_logic.py
from src.tax_logic import FirmFinancials, TCJAModel

def test_ebitda_regime_limit():
    """Tests the Pre-2022 logic (30% of EBITDA)."""
    model = TCJAModel()
    # 2021: Limit = 100 (EBITDA) * 0.3 = 30
    f = FirmFinancials(
        year=2021, 
        ebitda=100.0, 
        dep_and_amort=40.0, 
        interest_expense=50.0
    )
    assert model.get_deduction_limit(f) == 30.0

def test_ebit_regime_limit():
    """Tests the Post-2022 logic (30% of EBIT)."""
    model = TCJAModel()
    # 2022: Limit = (100 EBITDA - 40 D&A) * 0.3 = 18
    f = FirmFinancials(
        year=2022, 
        ebitda=100.0, 
        dep_and_amort=40.0, 
        interest_expense=50.0
    )
    assert model.get_deduction_limit(f) == 18.0

def test_pydantic_validation():
    """Ensures the model rejects negative financial values."""
    with pytest.raises(Exception):
        FirmFinancials(
            year=2022, 
            ebitda=-100.0, 
            dep_and_amort=0, 
            interest_expense=10
        )
