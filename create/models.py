from django.db import models

# Create your models here.

class createitems(models.Model):
    prod_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    cprod_id = models.CharField(max_length=100, primary_key=True)
    vendor = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100)
    quantity = models.IntegerField()
