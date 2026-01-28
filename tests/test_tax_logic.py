from pydantic import BaseModel, Field

class FirmFinancials(BaseModel):
    year: int = Field(..., ge=1990) # Expanded range for 'pre_2017' tests
    ebitda: float = Field(..., ge=0)
    dep_and_amort: float = Field(..., ge=0)
    interest_expense: float = Field(..., ge=0)

    @property
    def ebit(self) -> float:
        return self.ebitda - self.dep_and_amort

class TCJAModel:
    def __init__(self, limit_ratio: float = 0.30, regime: str = 'tcja_early'):
        self.limit_ratio = limit_ratio
        self.regime = regime

    def get_deduction_limit(self, firm: FirmFinancials) -> float:
        # Pre-2017: No Section 163(j) cap (effectively infinity)
        if self.regime == 'pre_2017' or firm.year < 2018:
            return float('inf')
        
        # TCJA Early (2018-2021): 30% of EBITDA
        if self.regime == 'tcja_early' or (2018 <= firm.year < 2022):
            return firm.ebitda * self.limit_ratio
            
        # TCJA Late (2022-Present): 30% of EBIT
        return firm.ebit * self.limit_ratio
