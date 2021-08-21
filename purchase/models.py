from enum import Enum
from django.db import models
from django.db.models import Sum
from partner.models import Partner
from product.models import Product

# Create your models here.
class PurchaseStatus(Enum):
    STARTED = "STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Purchase(models.Model):
    
    status = models.CharField(choices=PurchaseStatus.choices(), max_length=128, default=PurchaseStatus.STARTED.value)
    purchaseDate = models.DateField(null=False)
    comments = models.CharField(max_length=2048, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(null=False, max_digits=6, decimal_places=2, default=0.0)

    # relationships
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=False)
    products = models.ManyToManyField(Product)
    opportunity = models.ForeignKey('purchase_opportunity.PurchaseOpportunity', on_delete=models.PROTECT, null=True)

    def calculate_product_total_amount(self):
        products = self.products.all()
        total = sum(map(lambda p: p.unit_price, products))
        self.amount = total