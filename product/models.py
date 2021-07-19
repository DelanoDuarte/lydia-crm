from product_category.models import ProductCategory
from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=255)
    unit_price = models.FloatField()
    active = models.BooleanField(default=True)

    # relationships
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f'{self.name}'