from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    """
    Contact model is to save their personal contact info
    like First name, Last name, and bank detailas.
    """
    admin = models.ForeignKey(User, blank=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    iban = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name+self.last_name

