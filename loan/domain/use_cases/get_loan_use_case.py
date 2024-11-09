from dependency_injector.wiring import Provide

from loan.data.abstract_repo import LoanAbstractRepository
from loan.presentation.types import GetLoanResponse


class GetLoanUseCase:
    def __init__(
        self,
        db_repo: LoanAbstractRepository = Provide["loan_db_repo"]
    ) -> None:
        self.db_repo = db_repo

    def execute(self, loan_id: int) -> GetLoanResponse:
        loan = self.db_repo.get(loan_id)
        return GetLoanResponse(
            loan_id=loan.id,
            customer=loan.customer,
            loan_amount=loan.loan_amount,
            interest_rate=loan.interest_rate,
            monthly_installment=loan.monthly_payment,
            tenure=loan.tenure,
        )
