import os
import pandas as pd

from typing import List
from celery import shared_task

from customer.models import Customer
from loan.models import Loan


@shared_task
def migrate_initial_customer_data():
    customer_data_excel_path = os.path.join('assets', 'initial_data', 'customer_data.xlsx')

    data = pd.read_excel(customer_data_excel_path, engine='openpyxl')

    customer_data: List[Customer] = [
        Customer(
            first_name = row['First Name'],
            last_name = row['Last Name'],
            age = row['Age'],
            phone_number = row['Phone Number'],
            monthly_salary = row['Monthly Salary'],
            approved_limit = row['Approved Limit']
        )
        for _, row in data.iterrows()
    ]
    Customer.objects.bulk_create(customer_data)


@shared_task
def migrate_initial_loan_data():
    loan_data_excel_path = os.path.join('assets', 'initial_data', 'loan_data.xlsx')

    data = pd.read_excel(loan_data_excel_path, engine='openpyxl')

    # Convert the date columns to datetime format
    data['Date of Approval'] = pd.to_datetime(data['Date of Approval'], errors='coerce')
    data['End Date'] = pd.to_datetime(data['End Date'], errors='coerce')

    loan_data: List[Loan] = [
        Loan(
            customer_id = row['Customer ID'],
            loan_amount = row['Loan Amount'],
            tenure = row['Tenure'],
            interest_rate = row['Interest Rate'],
            monthly_payment = row['Monthly payment'],
            emis_paid_on_time = row['EMIs paid on Time'],
            approval_date = row['Date of Approval'],
            end_date = row['End Date'],
        )
        for _, row in data.iterrows()
    ]
    Loan.objects.bulk_create(loan_data)
