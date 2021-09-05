from typing import Dict

from partner.serializers import PartnerSerializer
from product.serializers import ProductSerializer
from purchase_opportunity.serializers import PurchaseOpportunityListSerializer
from rest_framework import serializers

from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    # relationships
    partner = PartnerSerializer()
    products = ProductSerializer(many=True)
    opportunity = PurchaseOpportunityListSerializer(many=False)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'purchaseDate',
            'status',
            'comments',
            'partner',
            'products',
            'opportunity',
            'amount'
        )

class PurchaseCreateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)
    comments = serializers.CharField(required=False)
    amount = serializers.DecimalField(required=True, max_digits=6, decimal_places=2)
    class Meta:
        model=Purchase
        fields=(
            "purchaseDate",
            "comments",
            "status",
            "products",
            "partner",
            "amount"
        )

    def create(self, validated_data: Dict):
        products_data = validated_data.pop('products')
        purchase: Purchase
        purchase = Purchase.objects.create(**validated_data)
        if products_data:
            for product in products_data:
                purchase.products.add(product)
                
        purchase.calculate_product_total_amount()
        return purchase
