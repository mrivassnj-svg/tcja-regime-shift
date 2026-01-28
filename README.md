# TCJA Regime Shift: Quantitative Modeling of IRC § 163(j)

## Project Overview
This repository provides a high-fidelity simulation of the interest deduction limitations introduced by the **Tax Cuts and Jobs Act (TCJA)**. Specifically, it models the structural "Regime Shift" that occurred on **January 1, 2022**, when the calculation for **Adjusted Taxable Income (ATI)** transitioned from an **EBITDA-based proxy** to an **EBIT-based proxy**.  

This shift creates a "Kink Point" in corporate debt capacity, particularly for **capital-intensive industries** with high **Depreciation and Amortization (D&A)**.

---

## Key Features

- **Multi-Regime Logic**: Supports `pre_2017` (uncapped), `tcja_early` (EBITDA), and `tcja_late` (EBIT) modeling.  
- **Hardened Data Validation**: Uses **Pydantic** to ensure financial inputs are economically valid.  
- **Automated Testing**: Full **CI/CD suite via GitHub Actions** to verify mathematical accuracy.  
- **Academic Rigor**: Includes **LaTeX documentation** (`docs/proofs.tex`) defining the underlying tax law.  

---

## The "Regime Shift" Benchmark

Using the included `scripts/run_benchmark.py`, we can observe the impact on a firm with **$100M EBITDA** and **$45M D&A**:

| Regime        | Deduction Limit | Disallowed Interest | Tax Shield Loss |
|---------------|----------------|-------------------|----------------|
| Pre-2022 (EBITDA) | $30.00M       | $10.00M           | $2.10M         |
| Post-2022 (EBIT)  | **$16.50M**   | $23.50M           | $4.94M         |

**Insight**: The 2022 transition effectively reduced this firm's interest deduction limit by **45%**, more than doubling the tax drag on their interest expense.

---

tcja-regime-shift/
├── .github/
│   └── workflows/          # Automated CI/CD Testing (GitHub Actions)
├── data/
│   ├── raw/                # Source CSVs / Raw financial inputs
│   └── processed/          # Outputs from cleaning and modeling
├── docs/
│   └── proofs.tex          # LaTeX documentation of IRC § 163(j) math
├── src/
│   ├── __init__.py         # Exposes classes for package-level imports
│   ├── tax_logic.py        # Core engine: Finite State Machine for regimes
│   └── visualization.py    # Plotting wrappers for "Kink Point" analysis
├── tests/
│   ├── __init__.py         # Allows pytest to recognize the test suite
│   ├── test_tax_logic.py   # Unit tests for core calculation accuracy
│   └── test_tradeoff.py    # Regression tests for regime shifts
├── pyproject.toml          # Modern Python build/dependency config
├── Makefile                # Automation for install, test, and clean
└── README.md               # Project overview and benchmark results

---

## Quick Start

### Install Dependencies

```bash
pip install -e .
Run Validation Tests
pytest tests/
Generate Benchmark
python scripts/run_benchmark.py
Future Development
 Integration with SEC EDGAR API for automated firm data retrieval.

 Monte Carlo simulations for varying interest rate environments.

 Interactive dashboard via Streamlit.
