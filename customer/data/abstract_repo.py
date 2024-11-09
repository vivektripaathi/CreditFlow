import abc

from customer.domain.domain_models import CustomerDoaminModel

class CustomerAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, request_data: CustomerDoaminModel) -> CustomerDoaminModel:
        """Create a Customer"""

    @abc.abstractmethod
    def get(self, customer_id: int) -> CustomerDoaminModel:
        """Get a Customer by id"""