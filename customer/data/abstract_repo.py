import abc

from customer.domain.domain_models import CustomerDoaminModel

class CustomerAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, request_data: CustomerDoaminModel) -> CustomerDoaminModel:
        """Create a Customer"""