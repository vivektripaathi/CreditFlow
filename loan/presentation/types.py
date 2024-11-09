from pydantic import BaseModel


class CheckLoanEligibilityRequest(BaseModel):
    customer_id: int
    loan_amount: int
    interest_rate: float
    tenure: int


class CheckLoanEligibilityResponse(BaseModel):
    customer_id: int
    approval: bool
    loan_amount: int
    interest_rate: float
    corrected_interest_rate: float
    tenure: int
    monthly_installment: float

class CreditScoreFactors(BaseModel):
    loan_sum: int
    tenures: int
    emis_paid_on_time: int
    loans_this_year: int
