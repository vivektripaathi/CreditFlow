import sys

from django.apps import AppConfig
from django.db import connection


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if 'runserver' not in sys.argv:
            print(sys.argv)
            return
        with connection.cursor() as cursor:
            from customer.models import Customer
            from loan.models import Loan
            from core.tasks import migrate_initial_customer_data, migrate_initial_loan_data

            customer_check = Customer.objects.exists()
            loan_check = Loan.objects.exists()

            if(not customer_check):
                migrate_initial_customer_data.delay()
            if(not loan_check):
                migrate_initial_loan_data.delay()

        print("Function to seed initial using background workers executed successfully.")
