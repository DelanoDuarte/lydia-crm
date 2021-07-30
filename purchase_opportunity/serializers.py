from product.serializers import ProductSerializer
from .models import PurchaseOpportunity
from partner.serializers import PartnerSerializer
from rest_framework import serializers

class PurchaseOpportunityCreateSerializer(serializers.ModelSerializer):

    comments = serializers.CharField(required=False)

    class Meta:
        model = PurchaseOpportunity
        fields=(
            'expectedEndingDate',
            'priority',
            'status',
            'comments',
            'partner',
            'products'
        ) 
    
    def save(self, **kwargs):
        return PurchaseOpportunity.objects.create(**kwargs)

class PurchaseOpportunityListSerializer(serializers.ModelSerializer):

    partner = PartnerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = PurchaseOpportunity
        fields=(
            'id',
            'expectedEndingDate',
            'priority',
            'status',
            'comments',
            'createdAt',
            'partner',
            'products'
        )
