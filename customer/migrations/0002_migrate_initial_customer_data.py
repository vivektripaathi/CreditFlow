from django.db import migrations
from typing import List
import pandas as pd
import os

def migrate_initial_data(apps, schema_editor):
    Customer = apps.get_model('customer', 'Customer')
    customer_data_excel_path = os.path.join('assets', 'initial_data', 'customer_data.xlsx')

    data = pd.read_excel(customer_data_excel_path, engine='openpyxl')

    customer_data: List[Customer] = [
        Customer(
            id = row['Customer ID'],
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


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_initial_data),
    ]
