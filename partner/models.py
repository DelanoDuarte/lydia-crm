from enum import Enum
from partner_type.models import PartnerType
from address.models import Address
from django.db import models

# Create your models here.
class Gender(Enum):
    MR = "MR"
    MRS = "MRS"
    MS = "MS"
    UNDEFINED = "UNDEFINED" 

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def values(cls):
        return list((i.value) for i in cls)

class Partner(models.Model):

    firstName = models.CharField(max_length=256, null=False)
    lastName = models.CharField(max_length=256, null=False)
    gender = models.CharField(choices=Gender.choices(), max_length=128, default=Gender.UNDEFINED.value)
    birthDate = models.DateField(null=True)
    age = models.IntegerField(null=True)
    mobile = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=128)
    website = models.CharField(max_length=512, null=True)
    firstContactDate = models.DateTimeField(null=True)
    comments = models.CharField(max_length=2048, null=True)

    partnerType = models.ForeignKey(PartnerType, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=False)

    slug = models.SlugField(null=True)

    def __str__(self) -> str:
        return f'{self.full_name()}'

    def full_name(self):
        return f'{self.firstName} {self.lastName}'

    def get_absolute_url(self):
        return f'/{self.slug}/'