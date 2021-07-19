from typing import Dict
from partner.serializers import PartnerSerializer
from product.serializers import ProductSerializer
from rest_framework import serializers

from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    # relationships
    partner = PartnerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'purchaseDate',
            'status',
            'comments',
            'partner',
            'products'
        )

class PurchaseCreateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)    
    class Meta:
        model=Purchase
        fields=(
            "comments",
            "status",
            "products",
            "partner"
        )

    def create(self, validated_data: Dict):
        products_data = validated_data.pop('products')
        purchase = Purchase.objects.create(**validated_data)
        if products_data:
            for product in products_data:
                purchase.products.add(product)
        return purchase