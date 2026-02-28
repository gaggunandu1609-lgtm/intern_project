from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE = (
        ('customer', 'Customer'),
        ('provider', 'Provider'),
    )

    role = models.CharField(max_length=20, choices=ROLE)
    phone = models.CharField(max_length=15, null=True, blank=True)