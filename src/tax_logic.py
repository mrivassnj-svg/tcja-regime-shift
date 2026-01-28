from pydantic import BaseModel, Field, validator
from typing import Literal

class FirmFinantials(BaseModel):
    year: int = Field(..., ge=2018)
    ebitda: float = Field(..., ge=0)
    depreciation_amortization: float = Field(..., ge=0)
    interest_expense: float = Field(..., ge=0)

    @property
    def ebit(self) -> float:
        return self.ebitda - self.depreciation_amortization

class TCJAModel:
    """Handles Section 163(j) interest deduction logic."""
    
    def __init__(self, limit_ratio: float = 0.30):
        self.limit_ratio = limit_ratio

    def calculate_deduction_limit(self, financials: FirmFinantials) -> float:
        # Pre-2022: Limit based on EBITDA
        if financials.year < 2022:
            base_metric = financials.ebitda
        # 2022 and Later: Limit based on EBIT (EBITDA - D&A)
        else:
            base_metric = financials.ebit
        
        return max(0, base_metric * self.limit_ratio)

    def get_tax_shield_impact(self, financials: FirmFinantials) -> dict:
        limit = self.calculate_deduction_limit(financials)
        deductible_interest = min(financials.interest_expense, limit)
        disallowed_interest = max(0, financials.interest_expense - limit)
        
        return {
            "limit": limit,
            "deductible_interest": deductible_interest,
            "disallowed_interest": disallowed_interest,
            "regime": "EBITDA-based" if financials.year < 2022 else "EBIT-based"
        }
