from django.db import models
from accounts.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProviderProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    experience = models.IntegerField()
    location = models.CharField(max_length=200)
    price = models.IntegerField()