import pytest
from src import TCJAModel, FirmFinancials

def test_init():
    # This checks if the import from src/__init__.py works
    model = TCJAModel()
    assert model.limit_ratio == 0.30
