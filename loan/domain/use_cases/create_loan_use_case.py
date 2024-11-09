from dateutil.relativedelta import relativedelta
from datetime import datetime, timezone
from dependency_injector.wiring import Provide

from customer.domain.use_cases.get_customer_use_case import GetCustomerUseCase
from loan.data.abstract_repo import LoanAbstractRepository
from loan.domain.domain_models import LoanDomainModel
from loan.domain.use_cases.check_loan_eligibility_use_case import CheckLoanEligibilityUseCase
from loan.exceptions import NotEligibleForLoanError
from loan.presentation.types import CreateLoanRequest, CreateLoanResponse


class CreateLoanUseCase:
    def __init__(
        self,
        db_repo: LoanAbstractRepository = Provide["loan_db_repo"],
        get_customer_use_case: GetCustomerUseCase = Provide["get_customer_use_case"],
        check_loan_eligibility_use_case: CheckLoanEligibilityUseCase = Provide["check_loan_eligibility_use_case"],
    ) -> None:
        self.db_repo = db_repo
        self.get_customer_use_case = get_customer_use_case
        self.check_loan_eligibility_use_case = check_loan_eligibility_use_case


    def execute(self, loan_request: CreateLoanRequest) -> CreateLoanResponse:
        self.get_customer_use_case.execute(loan_request.customer_id)
        response_message = ""
        try:
            loan_eligibility_response = self.check_loan_eligibility_use_case.execute(loan_request)
            eligible_for_loan = True
        except NotEligibleForLoanError as exc:
            eligible_for_loan = False
            response_message = exc.detail

        created_loan = None
        if(eligible_for_loan):
            created_loan = self.db_repo.create(
                loan_request=LoanDomainModel(
                    customer_id=loan_request.customer_id,
                    loan_amount=loan_request.loan_amount,
                    tenure=loan_request.tenure,
                    interest_rate=loan_eligibility_response.corrected_interest_rate,
                    monthly_payment=loan_eligibility_response.monthly_installment,
                    emis_paid_on_time=0,
                    approval_date=datetime.now(timezone.utc),
                    end_date = datetime.now(timezone.utc) + relativedelta(months=loan_request.tenure)
                )
            )
            response_message = "Loan Granted Successfully"
        return CreateLoanResponse(
            loan_id=created_loan.id if eligible_for_loan else None,
            customer_id=loan_request.customer_id,
            loan_approved=True if eligible_for_loan else False,
            message=response_message,
            monthly_installment=created_loan.monthly_payment if eligible_for_loan else None
        )
