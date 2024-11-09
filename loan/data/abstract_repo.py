import abc

from loan.domain.domain_models import LoanDomainModel, LoanListDomainModel

class LoanAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def bulk_get(self, customer_id: int) -> LoanListDomainModel:
        """Bulk get loans by customer id"""

    @abc.abstractmethod
    def get(self, loan_id: int) -> LoanDomainModel:
        """Get loan by id"""

    @abc.abstractmethod
    def create(self, loan_request: LoanDomainModel) -> LoanDomainModel:
        """Create a new loan entry"""