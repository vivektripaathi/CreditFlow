from dependency_injector import containers, providers

from loan.data.abstract_repo import LoanAbstractRepository
from loan.data.db_repo import LoanDbRepository
from loan.domain.use_cases.bulk_get_loans_use_case import BulkGetLoansUseCase

class LoanConainter(containers.DeclarativeContainer):
    loan_db_repo = providers.Dependency(
        instance_of=LoanAbstractRepository,
        default=LoanDbRepository(),
    )
    bulk_get_loans_use_case = providers.Factory(BulkGetLoansUseCase)