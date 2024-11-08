from django.urls import include, path

from customer.presentation import urls as customer_urls
app_name = "customer"

urlpatterns = [
    path("", include(customer_urls)),
]
