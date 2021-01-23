from django.db import models
from datetime import datetime
# Create your models here.

class device(models.Model):
    prod_id = models.CharField(max_length=100)
    device_sl = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, primary_key=True)
    device_bcode = models.CharField(max_length=100)
    device_date = models.CharField(max_length=100)
    device_hsn = models.IntegerField(len('device_hsn'))
