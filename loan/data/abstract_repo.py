import abc

from loan.domain.domain_models import LoanDomainModel, LoanListDomainModel

class LoanAbstractRepository(abc.ABC):
    def bulk_get(self, customer_id: int) -> LoanListDomainModel:
        """Bulk get loans by customer id"""
    
    def get(self, loan_id: int) -> LoanDomainModel:
        """Get loan by id"""