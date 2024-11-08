from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dependency_injector.wiring import Provide
import json
from CreditFlow.utils import dict_serialized
from loan.domain.use_cases.bulk_get_loans_use_case import BulkGetLoansUseCase

class BulkGetLoanView(APIView):
    def get(
        self,
        request,
        customer_id: int,
        bulk_get_loans_use_case: BulkGetLoansUseCase = Provide["bulk_get_loans_use_case"]
    ):
        response = bulk_get_loans_use_case.execute(customer_id)
        return Response(data=dict_serialized(response), status=status.HTTP_200_OK)

