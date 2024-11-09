from dependency_injector.wiring import Provide

from customer.data.abstract_repo import CustomerAbstractRepository
from customer.domain.domain_models import CustomerDoaminModel


class GetCustomerUseCase:
    def __init__(
        self,
        db_repo: CustomerAbstractRepository = Provide["db_repo"],
    ) -> None:
        self.db_repo = db_repo

    def execute(self, customer_id: int) -> CustomerDoaminModel:
        return self.db_repo.get(customer_id)