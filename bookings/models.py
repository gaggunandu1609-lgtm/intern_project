from django.db import models
from accounts.models import User
from services.models import ProviderProfile

class Booking(models.Model):

    STATUS = (
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('completed','Completed'),
    )

    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    provider = models.ForeignKey(
        ProviderProfile,on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='pending'
    )