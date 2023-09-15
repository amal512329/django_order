

# Create your models here.
from django.db import models

# Create your models here.

class LicenseOrder(models.Model):
    start_date = models.DateField(max_length=40,)
    subscription_id = models.CharField(max_length=255)
    commitment_or_billing = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255,)
    domain_name = models.CharField(max_length=255)
    qty = models.IntegerField()
    license_type = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    current_active_qty = models.IntegerField()
    erp = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    qut_no = models.CharField(max_length=255)
    invoice_no = models.CharField(max_length=255)
    create_sales_order = models.BooleanField(default=False)

    def __str__(self):
        return f"License Order - {self.subscription_id}"