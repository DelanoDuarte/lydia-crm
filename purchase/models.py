from enum import Enum
from django.db import models
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
    
    status = models.CharField(choices=PurchaseStatus.choices(), max_length=128, default=PurchaseStatus.STARTED.__str__)
    purchaseDate = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=2048, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    # relationships
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=False)
    products = models.ManyToManyField(Product)
    opportunity = models.ForeignKey('purchase_opportunity.PurchaseOpportunity', on_delete=models.PROTECT, null=True)