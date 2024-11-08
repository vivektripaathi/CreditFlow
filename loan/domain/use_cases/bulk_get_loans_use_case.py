from loan.data.abstract_repo import LoanAbstractRepository
from loan.domain.domain_models import LoanListDomainModel
from dependency_injector.wiring import Provide


class BulkGetLoansUseCase:
    def __init__(
        self,
        db_repo: LoanAbstractRepository = Provide["loan_db_repo"]
    ) -> None:
        self.db_repo = db_repo

    def execute(self, customer_id: int) -> LoanListDomainModel:
        # TODO: Map response as per requirement (A response type is to be created)
        return self.db_repo.bulk_get(customer_id)
