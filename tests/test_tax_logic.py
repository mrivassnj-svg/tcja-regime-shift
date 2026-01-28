import pytest
from src.tax_logic import FirmFinancials, TCJAModel

def test_logic():
    model = TCJAModel()
    f = FirmFinancials(year=2021, ebitda=100, dep_and_amort=40, interest_expense=50)
    # 100 * 0.3 = 30
    assert model.get_deduction_limit(f) == 30.0
