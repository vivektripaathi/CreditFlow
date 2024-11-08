from django.urls import include, path

from loan.presentation import urls as loan_urls
app_name = "loan"


urlpatterns = [
    path("", include(loan_urls)),
]