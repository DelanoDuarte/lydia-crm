from payment_mode.models import PaymentMode
from django.db import models
from partner.models import Partner
from purchase.models import Purchase

# Create your models here.
class Payment(models.Model):

    amount = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    paymentNumber = models.CharField(null=False, max_length=512)
    paymentDate = models.DateField(null=False)
    notes = models.TextField(null=True)

    # relationships
    mode = models.ForeignKey(PaymentMode, null=False, on_delete=models.PROTECT)
    purchase = models.ForeignKey(Purchase, null=False, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partner, null=False, on_delete=models.PROTECT)