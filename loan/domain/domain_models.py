from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from customer.domain.domain_models import CustomerDoaminModel


class LoanDomainModel(BaseModel):
    id: Optional[int]
    customer_id: int
    customer: Optional[CustomerDoaminModel] = None
    loan_amount: int
    tenure: int
    interest_rate: float
    monthly_payment: int
    emis_paid_on_time: int
    approval_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True


class LoanListDomainModel(BaseModel):
    __root__: List[LoanDomainModel]

    def __iter__(self):
        return iter(self.__root__)

    def __len__(self):
        return len(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]
