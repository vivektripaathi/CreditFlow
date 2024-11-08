from django.db import IntegrityError
from customer.data.abstract_repo import CustomerAbstractRepository
from customer.domain.domain_models import CustomerDoaminModel
from customer.exceptions import CustomerAlreadyExistsException
from customer.models import Customer

class CustomerDbRepository(CustomerAbstractRepository):
    def create(self, request_data: CustomerDoaminModel) -> CustomerDoaminModel:
        """Create a Customer"""
        try:
            customer_db_entry = Customer.objects.create(
                # id=request_data.id,
                first_name=request_data.first_name,
                last_name=request_data.last_name,
                age=request_data.age,
                phone_number=request_data.phone_number,
                monthly_salary=request_data.monthly_salary,
                approved_limit=request_data.approved_limit,
            )
            print(customer_db_entry.id)
            return CustomerDoaminModel.from_orm(customer_db_entry)
        except IntegrityError as exc:
            print(exc)
            raise CustomerAlreadyExistsException from exc
