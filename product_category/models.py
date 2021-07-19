from django.db import models

# Create your models here.
class ProductCategory(models.Model):

    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=2048, null=True)

    def __str__(self) -> str:
        return f'{self.name}'