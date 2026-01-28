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

## Repository Structure

tcja-regime-shift/
├── .github/workflows/ # Automated CI/CD Testing
├── data/ # Raw and processed financial datasets
├── docs/ # LaTeX proofs and methodology
├── src/ # Core engine: tax_logic.py & visualization.py
├── tests/ # Pytest suite for regime verification
├── pyproject.toml # Environment & dependency configuration
└── Makefile # One-word commands for installation and testing


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
