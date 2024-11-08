from django.urls import path

from loan.presentation.views import BulkGetLoanView

urlpatterns = [
    path('view_loans/<int:customer_id>/', BulkGetLoanView.as_view(), name="bulk_get_loans")
]

