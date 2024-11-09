from datetime import datetime, timezone
from typing import Tuple
from loan.data.abstract_repo import LoanAbstractRepository
from dependency_injector.wiring import Provide

from loan.domain.domain_models import LoanListDomainModel
from loan.exceptions import NotEligibleForLoanError
from loan.presentation.types import CreateLoanRequest, CheckLoanEligibilityResponse, CreditScoreFactors


class CheckLoanEligibilityUseCase:
    def __init__(
        self,
        db_repo: LoanAbstractRepository = Provide["loan_db_repo"]
    ) -> None:
        self.db_repo = db_repo


    def exctract_credit_score_factors(self, loans: LoanListDomainModel) -> CreditScoreFactors:
        current_year = datetime.now().year
        loans_this_year = 0
        tenures = 0
        emis_paid_on_time = 0
        loan_sum = 0

        for loan in loans:
            if loan.approval_date.year == current_year:
                loans_this_year += 1
            tenures += loan.tenure
            emis_paid_on_time += loan.emis_paid_on_time
            loan_sum += loan.loan_amount

        return CreditScoreFactors(
            tenures=tenures,
            emis_paid_on_time=emis_paid_on_time,
            loans_this_year=loans_this_year,
            loan_sum=loan_sum,
        )


    def get_credit_score(self, previous_loans: LoanListDomainModel) -> int:
        credit_score_factors = self.exctract_credit_score_factors(previous_loans)
        approved_limit = previous_loans[0].customer.approved_limit

        if credit_score_factors.loan_sum > approved_limit:
            raise NotEligibleForLoanError("Not eligible: total loans exceed your approved credit limit, resulting in a credit score of 0.")

        past_emi_score = min(100, (credit_score_factors.emis_paid_on_time / credit_score_factors.tenures) * 100)
        num_loans_score = max(0, 100 - abs(previous_loans.__len__()-5) * 10)
        loan_activity_score = max(0, 100 - credit_score_factors.loans_this_year * 20)
        approved_volume_score = min(100, 10 * (credit_score_factors.loan_sum / approved_limit))

        return int(
            past_emi_score * 0.40 +
            num_loans_score * 0.20 +
            loan_activity_score * 0.20 +
            approved_volume_score * 0.20
        )


    def get_current_emis(self, previous_loans: LoanListDomainModel) -> int:
        return sum(loan.monthly_payment for loan in previous_loans if loan.end_date > datetime.now(timezone.utc))


    def calculate_monthly_installment(self, principal: int, annual_interest_rate: float, tenure: int):
        monthly_interest_rate = annual_interest_rate / 12 / 100
        monthly_installment = (
            principal
            * monthly_interest_rate
            * ((1 + monthly_interest_rate) ** tenure)
        ) / (((1 + monthly_interest_rate) ** tenure) - 1)
        return monthly_installment


    def determine_loan_eligibility(
        self, credit_score: int, current_emis: int, monthly_salary: float, loan_request: CreateLoanRequest
    ) -> Tuple[bool, float]:
        if current_emis > 0.5 * monthly_salary:
            raise NotEligibleForLoanError("Not eligible: current EMIs exceed 50% of monthly salary.")
        
        if credit_score > 50:
            return True, loan_request.interest_rate
        elif 50 >= credit_score > 30:
            return True, 12.00
        elif 30 >= credit_score >= 10:
            return True, 16.00
        raise NotEligibleForLoanError


    def execute(self, loan_request: CreateLoanRequest):
        previous_loans = self.db_repo.bulk_get(loan_request.customer_id)
        credit_score = self.get_credit_score(previous_loans)
        current_emis = self.get_current_emis(previous_loans)
        approval, corrected_interest_rate = self.determine_loan_eligibility(
            credit_score, current_emis,
            previous_loans[0].customer.monthly_salary,
            loan_request
        )
        return CheckLoanEligibilityResponse(
            customer_id=loan_request.customer_id,
            approval=approval,
            loan_amount=loan_request.loan_amount,
            interest_rate=loan_request.interest_rate,
            corrected_interest_rate=corrected_interest_rate,
            tenure=loan_request.tenure,
            monthly_installment= self.calculate_monthly_installment(
                loan_request.loan_amount,
                corrected_interest_rate,
                loan_request.tenure
            ) if approval else 0.00
        )
