from django.urls import path

from loan.presentation.views import BulkGetLoanView, CheckLoanEligibilityView

urlpatterns = [
    path('view_loans/<int:customer_id>/', BulkGetLoanView.as_view(), name="bulk_get_loans"),
    path('check-eligibility/', CheckLoanEligibilityView.as_view(), name="bulk_loan_eligibility"),
]

