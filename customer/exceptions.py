from rest_framework import status, exceptions

class CustomerAlreadyExistsException(exceptions.APIException):
    code = "Customer_0001"
    default_detail = "Customer with same phone number already exists"
    status_code = status.HTTP_400_BAD_REQUEST
