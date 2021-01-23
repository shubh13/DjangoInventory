from django.db import models
from django.http import HttpResponseRedirect
from register.models import registeritems

class user_signup(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
