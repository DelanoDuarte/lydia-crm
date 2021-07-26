from django.db import models

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=128, null=False)
    alpha3Code = models.CharField(max_length=50, null=True)
    alpha2Code = models.CharField(max_length=50, null=True)

class Address(models.Model):

    mainAddress = models.CharField(max_length=256, null=False)
    additionalAddress = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=256, null=False)
    city = models.CharField(max_length=50, null=False)

    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
