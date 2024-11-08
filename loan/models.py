from django.db import models

# Create your models here.
class Loan(models.Model):
    customer = models.ForeignKey(
        "customer.Customer",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="%(class)s_customer",
    )
    loan_amount = models.IntegerField(blank=False, null=False)
    tenure = models.IntegerField(blank=False, null=False)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    monthly_payment = models.IntegerField(blank=False, null=False)
    emis_paid_on_time = models.IntegerField(blank=False, null=False)
    approval_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)

    class Meta:
        db_table = 'loans'