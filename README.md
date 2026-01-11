# TCJA Regime Shift Framework

A robust mathematical backbone for modeling the structural shift in U.S. corporate tax logic following the **Tax Cuts and Jobs Act (TCJA)**. This repository simulates how the transition from a linear tax benefit to a constrained, non-linear benefit affects corporate capital structure and the "Tradeoff Theory" of debt.

## 📚 Key Terminology

To fully understand the TCJA's impact, familiarize yourself with these core concepts:

- **§163(j) Limitation:** The IRS code section that restricts the deductibility of business interest expense. This is the primary "regime shift" mechanism.
- **ATI (Adjusted Taxable Income):** The tax-based earnings measure used as the base for the interest cap.
- **EBITDA:** Used as the proxy for ATI from 2018–2021 (Earnings Before Interest, Taxes, Depreciation, and Amortization).
- **EBIT:** Became the stricter proxy for ATI from 2022 onwards (subtracting Depreciation and Amortization), significantly impacting capital-intensive firms.
- **Tax Shield:** The reduction in tax liability resulting from deductible interest.
- **Kink Point:** The specific debt level where interest expense hits the 30% cap, causing the marginal tax benefit to drop to zero.

## 🗓️ Legislative Timeline

The model distinguishes between three eras of corporate finance based on the evolution of §163(j):

```text
       Pre-2018                  2018 - 2021                  2022 - Present
-----------------------|------------------------------|-------------------------------
  • 35% Corp Tax Rate    • 21% Corp Tax Rate            • 21% Corp Tax Rate
  • Full Interest        • §163(j) Cap (30% EBITDA)     • §163(j) Cap (30% EBIT)
    Deductibility        • Higher debt capacity         • Lower debt capacity for
  • Linear Tax Shield      (D&A neutral)                  high-D&A firms
                                                        • Stricter "Kink Point"
