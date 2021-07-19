from rest_framework import serializers
from .models import PartnerType

class PartnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerType
        fields = (
            'id',
            'name',
            'active'
        )
