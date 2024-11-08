from dependency_injector import containers, providers

from customer.data.abstract_repo import CustomerAbstractRepository
from customer.data.db_repo import CustomerDbRepository
from customer.domain.use_cases.register_customer_use_case import RegisterCustomerUseCase


class CustomerContainer(containers.DeclarativeContainer):
    db_repo = providers.Dependency(
        instance_of=CustomerAbstractRepository,
        default=CustomerDbRepository(),
    )
    register_customer_use_case = providers.Factory(RegisterCustomerUseCase)
