import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.tax_logic import TCJAModel, FirmFinantials

class TaxVisualizer:
    """Generates professional charts for TCJA Regime Shift analysis."""
    
    def __init__(self, style: str = "seaborn-v0_8-whitegrid"):
        plt.style.use(style)

    def plot_regime_comparison(self, ebitda: float, da: float, interest_range: np.ndarray):
        """
        Plots the 'Kink Point' comparing Pre-2022 (EBITDA) vs Post-2022 (EBIT) regimes.
        """
        model = TCJAModel()
        
        # Data preparation
        results = []
        for int_exp in interest_range:
            # Pre-2022 Scenario
            f_pre = FirmFinantials(year=2021, ebitda=ebitda, depreciation_amortization=da, interest_expense=int_exp)
            res_pre = model.get_tax_shield_impact(f_pre)
            
            # Post-2022 Scenario
            f_post = FirmFinantials(year=2022, ebitda=ebitda, depreciation_amortization=da, interest_expense=int_exp)
            res_post = model.get_tax_shield_impact(f_post)
            
            results.append({
                "interest_expense": int_exp,
                "pre_limit": res_pre['limit'],
                "post_limit": res_post['limit'],
                "pre_deductible": res_pre['deductible_interest'],
                "post_deductible": res_post['deductible_interest']
            })
            
        df = pd.DataFrame(results)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(df['interest_expense'], df['pre_deductible'], label='Pre-2022 (EBITDA Limit)', color='blue', lw=2)
        plt.plot(df['interest_expense'], df['post_deductible'], label='Post-2022 (EBIT Limit)', color='green', lw=2, linestyle='--')
        plt.plot(df['interest_expense'], df['interest_expense'], color='gray', linestyle=':', alpha=0.5, label='Total Interest')

        # Formatting
        plt.title(f"TCJA Regime Shift: Interest Deductibility Kink Point\n(EBITDA: ${ebitda}M, D&A: ${da}M)", fontsize=14)
        plt.xlabel("Total Interest Expense ($M)", fontsize=12)
        plt.ylabel("Deductible Interest ($M)", fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        return plt

if __name__ == "__main__":
    # Quick test run
    viz = TaxVisualizer()
    rng = np.linspace(0, 100, 50)
    viz.plot_regime_comparison(ebitda=100, da=40, interest_range=rng)
    plt.show()
