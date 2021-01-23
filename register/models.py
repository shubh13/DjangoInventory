from django.db import models
# Create your models here.

class registeritems(models.Model):
    emp_id = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.TextField(max_length=20)
