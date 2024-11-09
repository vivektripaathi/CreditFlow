from rest_framework import status, exceptions

class CustomerAlreadyExistsException(exceptions.APIException):
    code = "Customer_0001"
    default_detail = "Customer with same phone number already exists"
    status_code = status.HTTP_400_BAD_REQUEST


class CustomerDoesNotExistsException(exceptions.APIException):
    code = "Customer_0002"
    default_detail = "Customer with given id does not exists"
    status_code = status.HTTP_404_NOT_FOUND
