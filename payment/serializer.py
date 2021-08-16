from payment_mode.models import PaymentMode
from purchase.models import Purchase
from partner.models import Partner
from purchase.serializers import PurchaseSerializer
from partner.serializers import PartnerListSerializer
from payment.models import Payment
from rest_framework import serializers

class PaymentListSerializer(serializers.ModelSerializer):

    partner = PartnerListSerializer(many=False)
    purchase = PurchaseSerializer(many=False)

    class Meta:
        model = Payment
        fields=('__all__')


class PaymentCreateSerializer(serializers.ModelSerializer):

    notes = serializers.CharField(required=False)
    partner = serializers.PrimaryKeyRelatedField(queryset=Partner.objects)
    purchase = serializers.PrimaryKeyRelatedField(queryset=Purchase.objects)
    mode = serializers.PrimaryKeyRelatedField(queryset=PaymentMode.objects)
    amount = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Payment
        fields=(
            'partner',
            'purchase',
            'mode',
            'notes',
            'amount',
            'paymentNumber',
            'paymentDate'
        )

    def create(self, data):
        return Payment.objects.create(**data)