import pandas as pd
from src.tax_logic import TCJAModel, FirmFinancials

def run_benchmarks():
    # 1. Define a high-growth, high-CAPEX firm (High Depreciation)
    firm_data = FirmFinancials(
        year=2022, 
        ebitda=100.0, 
        dep_and_amort=45.0,  # High D&A significantly lowers EBIT
        interest_expense=40.0,
        tax_rate=0.21
    )

    # 2. Initialize the two competing regimes
    early_regime = TCJAModel(regime='tcja_early') # EBITDA-based
    late_regime = TCJAModel(regime='tcja_late')   # EBIT-based

    # 3. Calculate impacts
    results = []
    for name, model in [("Pre-2022 (EBITDA)", early_regime), ("Post-2022 (EBIT)", late_regime)]:
        limit = model.get_deduction_limit(firm_data)
        disallowed = max(0, firm_data.interest_expense - limit)
        tax_drag = disallowed * firm_data.tax_rate
        
        results.append({
            "Regime": name,
            "Deduction Limit": f"${limit:.2f}M",
            "Disallowed Interest": f"${disallowed:.2f}M",
            "Tax Shield Loss": f"${tax_drag:.2f}M"
        })

    # 4. Output Comparison Table
    df = pd.DataFrame(results)
    print("\n--- TCJA REGIME SHIFT BENCHMARK ---")
    print(f"Firm Profile: EBITDA $100M | D&A $45M | Interest $40M")
    print("-" * 50)
    print(df.to_string(index=False))
    print("-" * 50)
    print("Insight: The shift to EBIT reduces the deduction limit by 45%,")
    print("increasing the effective tax burden for capital-intensive firms.")

if __name__ == "__main__":
    run_benchmarks()
