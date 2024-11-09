from typing import List, Optional
from pydantic import BaseModel

from customer.domain.domain_models import CustomerDoaminModel


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

class BulkGetLoanResponse(BaseModel):
    loan_id: int
    loan_amount: int
    interest_rate: float
    monthly_installment: float
    repayments_left: int

class BulkGetLoanListResponse(BaseModel):
    __root__: List[BulkGetLoanResponse]


class GetLoanResponse(BaseModel):
    loan_id: int
    customer: Optional[CustomerDoaminModel] = None
    loan_amount: int
    interest_rate: float
    monthly_installment: int
    tenure: int
