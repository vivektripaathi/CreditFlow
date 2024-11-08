from django.db import migrations
from typing import List
import pandas as pd
import os

def migrate_initial_data(apps, schema_editor):
    Loan = apps.get_model('loan', 'Loan')
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

    Loan.objects.bulk_create(loan_data  )


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_initial_data),
    ]
