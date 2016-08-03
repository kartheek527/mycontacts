from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    admin = models.ForeignKey(User, blank=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    iban = models.CharField(max_length=200)

