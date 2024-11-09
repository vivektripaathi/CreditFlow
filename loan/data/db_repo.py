from loan.data.abstract_repo import LoanAbstractRepository
from loan.exceptions import LoanDoesNotExistsException
from loan.models import Loan
from loan.domain.domain_models import LoanDomainModel, LoanListDomainModel



class LoanDbRepository(LoanAbstractRepository):
    def bulk_get(self, customer_id: int) -> LoanListDomainModel:
        loan_db_list = Loan.objects.filter(customer_id=customer_id).select_related("customer")
        return LoanListDomainModel(
            __root__=list(
                map(LoanDomainModel.from_orm, loan_db_list)
            )
        )
    
    def get(self, loan_id: int) -> LoanDomainModel:
        try:
            loan_db_entry = Loan.objects.get(id=loan_id)
            return LoanDomainModel.from_orm(loan_db_entry)
        except Loan.DoesNotExist as exc:
            raise LoanDoesNotExistsException from exc

    def create(self, loan_request: LoanDomainModel) -> LoanDomainModel:
        loan_db_entry = Loan.objects.create(
            customer_id=loan_request.customer_id,
            loan_amount=loan_request.loan_amount,
            tenure=loan_request.tenure,
            interest_rate=loan_request.interest_rate,
            monthly_payment=loan_request.monthly_payment,
            emis_paid_on_time=loan_request.emis_paid_on_time,
            approval_date=loan_request.approval_date,
            end_date=loan_request.end_date,
        )
        return LoanDomainModel.from_orm(loan_db_entry)
