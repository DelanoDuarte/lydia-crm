from django.db.models.fields.files import ImageField
from product_category.models import ProductCategory
from django.db import models

from io import BytesIO

# Create your models here.

class ProductImage(models.Model):

    image = ImageField(upload_to="images/", blank=True, null=True)

    def image_url(self):
        if self.image:
            return f'http://127.0.0.1:8000{self.image.url}'
        return ''

class Product(models.Model):

    name = models.CharField(max_length=255)
    unit_price = models.FloatField()
    active = models.BooleanField(default=True)

    # relationships
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    images = models.ManyToManyField(ProductImage)
    
    def __str__(self) -> str:
        return f'{self.name}'


    def by_category(category_name: str):
        if category_name:
            return Product.objects.filter(product_category__name=category_name).all()
        return Product.objects.all()