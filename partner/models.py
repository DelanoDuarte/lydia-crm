from partner_type.models import PartnerType
from django.db import models

# Create your models here.
class Partner(models.Model):

    firstName = models.CharField(max_length=256, null=False)
    lastName = models.CharField(max_length=256, null=False)
    birthDate = models.DateField(null=True)
    age = models.IntegerField(null=True)
    mobile = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=128)
    website = models.CharField(max_length=512, null=True)
    firstContactDate = models.DateTimeField(null=True)
    comments = models.CharField(max_length=2048, null=True)

    partnerType = models.ForeignKey(PartnerType, on_delete=models.PROTECT)

    slug = models.SlugField(null=True)

    def __str__(self) -> str:
        return f'{self.full_name()}'

    def full_name(self):
        return f'{self.firstName} {self.lastName}'

    def get_absolute_url(self):
        return f'/{self.slug}/'