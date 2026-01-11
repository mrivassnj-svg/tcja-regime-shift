# Legislative & Mathematical References

### 1. The 163(j) Limitation Formula
The core of this model follows the Tax Cuts and Jobs Act (TCJA) amendment to §163(j), which restricts the business interest deduction to the sum of:
1. Business interest income.
2. 30% of **Adjusted Taxable Income (ATI)**.
3. Floor plan financing interest.

**In this model, we isolate ATI shift:**
* **2018–2021:** $ATI \approx EBITDA$ (Earnings Before Interest, Taxes, Depreciation, and Amortization).
* **2022–Present:** $ATI \approx EBIT$ (Earnings Before Interest and Taxes).

### 2. Tax Shield Calculation
The value of the tax shield ($V_{ts}$) in our framework is defined as:
$$V_{ts} = \tau \cdot \min(D \cdot r, \alpha \cdot \text{ATI})$$

Where:
- $\tau$ = Corporate Tax Rate (0.35 or 0.21)
- $D$ = Total Debt
- $r$ = Interest Rate
- $\alpha$ = 0.30 (The TCJA Cap)

### 3. Citations
* **Internal Revenue Service (IRS):** [Section 163(j) Limitation Overview](https://www.irs.gov/newsroom/basic-question-and-answers-about-the-limitation-on-the-deduction-for-business-interest-expense)
* **Congressional Budget Office (CBO):** [The Corporate Income Tax Under the TCJA](https://www.cbo.gov/publication/54644)
