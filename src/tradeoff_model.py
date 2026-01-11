import numpy as np

class TCJAModel:
    """
    Models corporate tax shield behavior under different U.S. tax regimes.
    Specifically isolates the impact of §163(j) interest deductibility caps.

    The model tracks the 'Regime Shift' from the pre-2017 environment to 
    the current post-2022 EBIT-constrained environment.
    """

    def __init__(self, regime='post_2022'):
        """
        Supported regimes:
        - 'pre_2017': 35% corp rate, effectively no interest cap.
        - 'tcja_early': 21% corp rate, 30% EBITDA cap (2018-2021).
        - 'post_2022': 21% corp rate, 30% EBIT cap (2022-Present).
        """
        self.regime = regime
        self.params = self._set_regime_params()

    def _set_regime_params(self):
        regimes = {
            'pre_2017': {
                'corp_tax_rate': 0.35,
                'interest_cap_pct': 1.0,
                'cap_base': 'ebitda',
                'label': 'Pre-2017 (35%)'
            },
            'tcja_early': {
                'corp_tax_rate': 0.21,
                'interest_cap_pct': 0.30,
                'cap_base': 'ebitda',
                'label': 'TCJA 2018–2021 (EBITDA)'
            },
            'post_2022': {
                'corp_tax_rate': 0.21,
                'interest_cap_pct': 0.30,
                'cap_base': 'ebit',
                'label': 'TCJA 2022+ (EBIT)'
            }
        }
        if self.regime not in regimes:
            raise ValueError(f"Invalid regime: {self.regime}. Choose from {list(regimes.keys())}")
        return regimes[self.regime]

    def _get_cap_limit(self, ebitda, da):
        """
        Calculates the dollar limit of the interest deduction based on the regime's base.
        Ensures a floor of 0.0 for the cap base (ATI).
        """
        cap_pct = self.params['interest_cap_pct']
        
        if self.regime == 'pre_2017':
            return np.inf
        
        # Calculate Adjusted Taxable Income (ATI) proxy
        if self.params['cap_base'] == 'ebitda':
            ati = max(0.0, ebitda)
        else:
            # Shift to EBIT: EBITDA - Depreciation & Amortization
            ati = max(0.0, ebitda - da)
            
        return cap_pct * ati

    def calculate_tax_shield(self, debt, interest_rate, ebitda, da=0.0):
        """
        Computes the dollar value of the tax shield: τ * min(Interest, Cap).
        """
        tau = self.params['corp_tax_rate']
        interest_expense = debt * interest_rate
        cap_limit = self._get_cap_limit(ebitda, da)
        
        deductible_interest = min(interest_expense, cap_limit)
        return tau * deductible_interest

    def marginal_benefit_of_debt(self, debt, interest_rate, ebitda, da=0.0):
        """
        Returns the tax benefit of the next $1 of debt. 
        Uses a 1e-9 tolerance to prevent floating-point comparison errors.
        """
        interest_expense = debt * interest_rate
        cap_limit = self._get_cap_limit(ebitda, da)
        
        # If interest is below the cap, benefit is the tax rate. Else, $0.
        if (cap_limit - interest_expense) > 1e-9:
            return self.params['corp_tax_rate']
        else:
            return 0.0
