from typing import List, Optional
from pydantic import BaseModel


class CustomerDoaminModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    age: int
    phone_number: str
    monthly_salary: float
    approved_limit: float

    class Config:
        orm_mode = True
