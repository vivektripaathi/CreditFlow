from loan.data.abstract_repo import LoanAbstractRepository
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
