from enum import Enum
from django.db import models
from partner.models import Partner
from product.models import Product
from purchase.models import Purchase

# Create your models here.
class PurchaseOpportunityStatus(Enum):
    NEW = "NEW"
    INTERESTED = "INTERESTED"
    ON_GOING = "ON_GOING" 
    CONVERTED = "CONVERTED"
    NOT_CONVERTED = "NOT_CONVERTED" 

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def values(cls):
        return list((i.value) for i in cls)

class PurchaseOpportunity(models.Model):

    code = models.CharField(max_length=128)
    expectedEndingDate = models.DateTimeField(null=False)
    priority = models.IntegerField(null=False, default=1)
    status = models.CharField(choices=PurchaseOpportunityStatus.choices(), max_length=128, default=PurchaseOpportunityStatus.NEW.__str__)
    comments = models.TextField(max_length=2048)
    createdAt = models.DateTimeField(auto_now_add=True)

    # relationship
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)

    def convert_to_purchase(self, id: int):

        # Update actual Opportunity
        opportunity = self.objects.get(id=id)
        opportunity.status = PurchaseOpportunityStatus.CONVERTED
        opportunity.save()

        # Create Purchase based on Opportunity
        purchase = Purchase(
            partner=opportunity.partner,
            products=opportunity.products,
            comments=opportunity.comments,
            opportunity=opportunity
        )
        purchase.save()

        return opportunity
