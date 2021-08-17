from payment_mode.models import PaymentMode
from rest_framework import serializers

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields=(
            "__all__"
        )