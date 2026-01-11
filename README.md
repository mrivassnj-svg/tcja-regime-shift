# TCJA Regime Shift Framework

A modular Python framework for analyzing corporate capital structure transitions under the Tax Cuts and Jobs Act (TCJA).

## 🚀 The Backbone
This project identifies the "kink" in the corporate tax shield caused by the 2017 legislative shift. It allows researchers to visualize how **Capital Intensity** (measured via Depreciation & Amortization) interacts with **Interest Deductibility**.

## 🛠️ Key Components
- **`TCJAModel`**: A robust class handling float-point precision and the EBITDA-to-EBIT transition.
- **Sensitivity Analysis**: Dynamic simulation of debt capacity across three distinct US tax regimes.
- **Dual-Plot Visuals**: Simultaneously tracks total tax shield value and the step-function of marginal benefits.

## 📊 Getting Started
1. Clone the repo: `git clone https://github.com/username/tcja-regime-shift.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Open `notebooks/TCJA_Regime_Shift_Framework.ipynb` to run the simulation.

## ⚖️ License
This framework is for sensitivity analysis and educational purposes, not causal inference or tax advice.

## 🔍 Key Empirical Insights

This model demonstrates the "Capital Intensity Penalty" introduced by the 2022 §163(j) transition. 

| Feature | Pre-2017 Regime | TCJA (2018-2021) | TCJA (2022-Present) |
| :--- | :--- | :--- | :--- |
| **Tax Shield Shape** | Linear (Infinite) | Kinked (EBITDA-based) | Kinked (EBIT-based) |
| **Max Benefit** | $0.35 per $1 interest | $0.21 per $1 interest | $0.21 per $1 interest |
| **D&A Sensitivity** | Neutral | Low | **High (Penalty)** |

### The "D&A Trap"
Under the current regime, firms with high Depreciation & Amortization (D&A) hit their debt capacity 30-40% sooner than they did in 2021, even with identical cash flows. This framework allows you to quantify that "Debt Gap."

## 📚 Key Terminology

To fully understand the TCJA's impact, familiarize yourself with these core concepts:

- **TCJA (Tax Cuts and Jobs Act of 2017):** Major U.S. tax reform that significantly altered corporate taxation.
- **§163(j) Limitation:** An IRS code section that restricts the deductibility of business interest expense. The core mechanism modeled in this repository.
- **ATI (Adjusted Taxable Income):** A tax-specific earnings measure used as the base for the §163(j) interest deduction cap. *Crucially, its calculation changed in 2022.*
- **EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization):** A common financial metric, used as the *proxy for ATI* from 2018–2021.
- **EBIT (Earnings Before Interest and Taxes):** A financial metric, which became the *proxy for ATI* from 2022 onwards (making the interest cap stricter for high D&A firms).
- **Tax Shield:** The reduction in a firm's tax liability due to the deductibility of interest expense.
- **Kink Point:** The specific level of corporate debt where the interest expense surpasses the §163(j) cap, causing the marginal tax shield to drop to zero. This creates a non-linear "kink" in the benefit curve.
