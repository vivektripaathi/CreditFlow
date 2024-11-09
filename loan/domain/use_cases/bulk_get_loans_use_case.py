from loan.data.abstract_repo import LoanAbstractRepository
from dependency_injector.wiring import Provide

from loan.presentation.types import BulkGetLoanResponse, BulkGetLoanListResponse


class BulkGetLoansUseCase:
    def __init__(
        self,
        db_repo: LoanAbstractRepository = Provide["loan_db_repo"]
    ) -> None:
        self.db_repo = db_repo

    def execute(self, customer_id: int) -> BulkGetLoanListResponse:
        loans = self.db_repo.bulk_get(customer_id)
        return BulkGetLoanListResponse(
            __root__=[
                BulkGetLoanResponse(
                    loan_id=loan.id,
                    loan_amount=loan.loan_amount,
                    interest_rate=loan.interest_rate,
                    monthly_installment=loan.monthly_payment,
                    repayments_left=(loan.tenure-loan.emis_paid_on_time)
                )
                for loan in loans
            ]
        )
