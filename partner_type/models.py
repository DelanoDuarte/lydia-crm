from django.db import models

# Create your models here.
class PartnerType(models.Model):

    name = models.CharField(max_length=256, null=False)
    active = models.BooleanField(null=False, default=True)