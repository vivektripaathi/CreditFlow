from dependency_injector.wiring import Provide

from customer.data.abstract_repo import CustomerAbstractRepository
from customer.domain.domain_models import CustomerDoaminModel
from customer.presentation.types import RegisterCustomerRequest



class RegisterCustomerUseCase:
    def __init__(
        self,
        db_repo: CustomerAbstractRepository = Provide["db_repo"]
    ) -> None:
        self.db_repo = db_repo


    def execute(self, customer_request: RegisterCustomerRequest) -> CustomerDoaminModel:
        a =  self.db_repo.create(
            CustomerDoaminModel(
                first_name=customer_request.first_name,
                last_name=customer_request.last_name,
                age=customer_request.age,
                phone_number=customer_request.phone_number,
                monthly_salary=customer_request.monthly_salary,
                approved_limit=36*customer_request.monthly_salary,
            )
        )
        return a
