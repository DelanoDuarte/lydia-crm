from django.db import models

# Create your models here.
class PaymentMode(models.Model):

    name = models.CharField(null=False, max_length=2048)
    active = models.BooleanField(default=True, null=False)

    def __str__(self) -> str:
        return f'{self.name}'