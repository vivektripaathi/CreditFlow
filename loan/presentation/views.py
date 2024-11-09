from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dependency_injector.wiring import Provide
from CreditFlow.utils import dict_serialized
from loan.domain.use_cases.bulk_get_loans_use_case import BulkGetLoansUseCase
from loan.domain.use_cases.check_loan_eligibility_use_case import CheckLoanEligibilityUseCase
from loan.domain.use_cases.create_loan_use_case import CreateLoanUseCase
from loan.domain.use_cases.get_loan_use_case import GetLoanUseCase
from loan.exceptions import NotEligibleForLoanError
from loan.presentation.types import CheckLoanEligibilityResponse, CreateLoanRequest

class BulkGetLoanView(APIView):
    def get(
        self,
        request,
        customer_id: int,
        bulk_get_loans_use_case: BulkGetLoansUseCase = Provide["bulk_get_loans_use_case"]
    ):
        response = bulk_get_loans_use_case.execute(customer_id)
        return Response(data=dict_serialized(response), status=status.HTTP_200_OK)


class CheckLoanEligibilityView(APIView):
    def post(
        self,
        request,
        check_loan_eligibility_use_case: CheckLoanEligibilityUseCase = Provide["check_loan_eligibility_use_case"],
    ):
        loan_request = CreateLoanRequest.parse_obj(request.data)
        try:
            response = check_loan_eligibility_use_case.execute(loan_request)
        except NotEligibleForLoanError:
            response = CheckLoanEligibilityResponse(
                customer_id=loan_request.customer_id,
                loan_amount=loan_request.loan_amount,
                interest_rate=loan_request.interest_rate,
                tenure=loan_request.tenure,
            )
        return Response(data=dict_serialized(response), status=status.HTTP_200_OK)


class GetLoanView(APIView):
    def get(
        self,
        request,
        loan_id: int,
        get_loan_use_case : GetLoanUseCase = Provide["get_loan_use_case"],
    ):
        response = get_loan_use_case.execute(loan_id)
        return Response(data=dict_serialized(response), status=status.HTTP_200_OK)


class CreateLoanView(APIView):
    def post(
        self,
        request,
        create_loan_use_case : CreateLoanUseCase = Provide["create_loan_use_case"],
    ): 
        loan_request = CreateLoanRequest.parse_obj(request.data)
        response = create_loan_use_case.execute(loan_request)
        return Response(data=dict_serialized(response), status=status.HTTP_201_CREATED)
