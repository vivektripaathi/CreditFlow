from rest_framework import status, exceptions

class LoanDoesNotExistsException(exceptions.APIException):
    code = "Loan_0001"
    default_detail = "Loan with given id does not exists"
    status_code = status.HTTP_404_NOT_FOUND

class NotEligibleForLoanError(exceptions.APIException):
    code = "Loan_0002"
    default_detail = "You are not eligible for this loan"
    status_code = status.HTTP_400_BAD_REQUEST
