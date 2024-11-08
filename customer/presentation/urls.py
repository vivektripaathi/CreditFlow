from django.urls import path

from customer.presentation.views import RegisterCustomerView

urlpatterns = [
    path('register/', RegisterCustomerView.as_view(), name='register_customer'),
]
