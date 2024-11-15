from dependency_injector import containers, providers

from loan.data.abstract_repo import LoanAbstractRepository
from loan.data.db_repo import LoanDbRepository
from loan.domain.use_cases.bulk_get_loans_use_case import BulkGetLoansUseCase
from loan.domain.use_cases.check_loan_eligibility_use_case import CheckLoanEligibilityUseCase
from loan.domain.use_cases.create_loan_use_case import CreateLoanUseCase
from loan.domain.use_cases.get_loan_use_case import GetLoanUseCase

class LoanConainter(containers.DeclarativeContainer):
    loan_db_repo = providers.Dependency(
        instance_of=LoanAbstractRepository,
        default=LoanDbRepository(),
    )
    bulk_get_loans_use_case = providers.Factory(BulkGetLoansUseCase)
    check_loan_eligibility_use_case = providers.Factory(CheckLoanEligibilityUseCase)
    get_loan_use_case = providers.Factory(GetLoanUseCase)
    create_loan_use_case = providers.Factory(CreateLoanUseCase)