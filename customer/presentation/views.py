from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dependency_injector.wiring import Provide

from customer.domain.use_cases.register_customer_use_case import RegisterCustomerUseCase
from customer.presentation.types import RegisterCustomerRequest

class RegisterCustomerView(APIView):
    def post(
        self,
        request,
        register_customer_use_case : RegisterCustomerUseCase = Provide["register_customer_use_case"],

    ):
        customer_request = RegisterCustomerRequest.parse_obj(request.data)
        print("\n Before use case call in view \n")
        response = register_customer_use_case.execute(customer_request)
        return Response(data = dict(response), status=status.HTTP_201_CREATED)

