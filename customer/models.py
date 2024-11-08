from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    age = models.PositiveIntegerField(blank=False, null=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    approved_limit = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'customers'
