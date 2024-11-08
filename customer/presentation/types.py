from pydantic import BaseModel

class RegisterCustomerRequest(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone_number: str
    monthly_salary: float
