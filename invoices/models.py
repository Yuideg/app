from datetime import datetime
from django.db import models
from rest_framework.exceptions import ValidationError


# Create your models here.
# Create Invoice model
def validate_date(value):
        today = datetime.now()
        if value >= today:
            return value
        else:
            raise ValidationError({"detail":"Date value must be valid."})

class Invoice(models.Model):

    class Meta:
        db_table = "invoices_invoice"
    invoice_no = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    date=models.DateField(auto_now=True,validators=[validate_date])



# Create InvoiceDetail Model
class InvoiceDetail(models.Model):

    class Meta:
        db_table = "invoices_invoice_detail"
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="details")
    description = models.TextField()
    quantity=models.DecimalField(max_digits=15,decimal_places=4)
    unit = models.CharField(max_length=20,choices=[("kg","Killo Gram"),("g","Gram")])
    price = models.DecimalField(max_digits=15,decimal_places=4,)

