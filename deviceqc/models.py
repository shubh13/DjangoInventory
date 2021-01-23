from django.db import models

# Create your models here.

class yes_deviceqc(models.Model):
    prod_id = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, primary_key=True)
    device_bcode = models.CharField(max_length=100)
    qc_passed = models.CharField(max_length=100)


class no_deviceqc(models.Model):
    prod_id = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, primary_key=True)
    device_bcode = models.CharField(max_length=100)
    qc_passed = models.CharField(max_length=100)
