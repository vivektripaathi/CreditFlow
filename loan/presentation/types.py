from typing import List, Optional
from pydantic import BaseModel

from customer.domain.domain_models import CustomerDoaminModel


class CheckLoanEligibilityResponse(BaseModel):
    customer_id: int
    approval: bool = False
    loan_amount: int
    interest_rate: float
    corrected_interest_rate: float = 0.00
    tenure: int
    monthly_installment: float = 0.00

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


class CreateLoanRequest(BaseModel):
    customer_id: int
    loan_amount: int
    interest_rate: float
    tenure: int


class CreateLoanResponse(BaseModel):
    loan_id: Optional[int] = None
    customer_id: int
    loan_approved: bool = False
    message: str
    monthly_installment: Optional[int] = None