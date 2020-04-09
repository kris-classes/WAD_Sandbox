from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    image = models.ImageField(null=True, blank=True)
    owner = models.ForeignKey('Owner', related_name='cars_owned_by', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.manufacturer} - {self.model}'



class Owner(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.address}'

