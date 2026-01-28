from pydantic import BaseModel, Field

class FirmFinancials(BaseModel):
    year: int = Field(..., ge=2018)
    ebitda: float = Field(..., ge=0)
    dep_and_amort: float = Field(..., ge=0)
    interest_expense: float = Field(..., ge=0)

    @property
    def ebit(self) -> float:
        return self.ebitda - self.dep_and_amort

class TCJAModel:
    def __init__(self, limit_ratio: float = 0.30):
        self.limit_ratio = limit_ratio

    def get_deduction_limit(self, firm: FirmFinancials) -> float:
        # Pre-2022: EBITDA | Post-2022: EBIT
        base = firm.ebitda if firm.year < 2022 else firm.ebit
        return max(0, base * self.limit_ratio)
