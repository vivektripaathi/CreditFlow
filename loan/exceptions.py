from rest_framework import status, exceptions

class LoanDoesNotExistsException(exceptions.APIException):
    code = "Loan_0001"
    default_detail = "Loan with given id does not exists"
    status_code = status.HTTP_404_NOT_FOUND
