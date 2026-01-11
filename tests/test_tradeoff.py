import pytest
import numpy as np
from src import TCJAModel

def test_pre_2017_linearity():
    """Verify that Pre-2017 shields are linear and uncapped."""
    model = TCJAModel(regime='pre_2017')
    # Under 35% rate, $1000 interest should yield $350 shield
    assert model.calculate_tax_shield(debt=10000, interest_rate=0.10, ebitda=100) == 350.0

def test_163j_cap_binding():
    """Verify that the 30% EBITDA cap binds correctly in early TCJA."""
    model = TCJAModel(regime='tcja_early')
    ebitda = 1000.0
    interest_rate = 0.10
    
    # Max deductible interest = 30% of 1000 = $300
    # Debt of $5000 @ 10% = $500 interest (exceeds cap)
    # Expected shield = $300 * 0.21 = $63
    shield = model.calculate_tax_shield(debt=5000, interest_rate=interest_rate, ebitda=ebitda)
    assert np.isclose(shield, 63.0)

def test_ebit_vs_ebitda_shift():
    """Verify the 2022 shift from EBITDA to EBIT reduces debt capacity."""
    early_model = TCJAModel(regime='tcja_early')
    post_model = TCJAModel(regime='post_2022')
    
    ebitda = 1000.0
    da = 500.0 # High depreciation
    debt = 5000.0
    rate = 0.10 # $500 interest expense
    
    # Early (EBITDA): Cap is 300. Shield = 300 * 0.21 = 63
    # Post (EBIT): Cap is 30% of (1000-500) = 150. Shield = 150 * 0.21 = 31.5
    shield_early = early_model.calculate_tax_shield(debt, rate, ebitda, da)
    shield_post = post_model.calculate_tax_shield(debt, rate, ebitda, da)
    
    assert shield_early > shield_post
    assert np.isclose(shield_post, 31.5)

def test_precision_tolerance():
    """Verify marginal benefit handles float precision near the kink."""
    model = TCJAModel(regime='tcja_early')
    # Cap is 30.0. Interest is exactly 30.00000000001
    ebitda = 100.0
    debt = 300.0000000001
    rate = 0.1
    
    mbd = model.marginal_benefit_of_debt(debt, rate, ebitda)
    assert mbd == 0.0
