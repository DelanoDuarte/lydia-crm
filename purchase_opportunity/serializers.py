from typing import Dict, Tuple
from product.models import Product
from partner.models import Partner
from product.serializers import ProductListSerializer, ProductSerializer
from .models import PurchaseOpportunity
from partner.serializers import PartnerSerializer
from rest_framework import serializers

class PurchaseOpportunityCreateSerializer(serializers.ModelSerializer):

    comments = serializers.CharField(required=False)
    partner = serializers.PrimaryKeyRelatedField(queryset=Partner.objects)
    products = serializers.ListField(
        child = serializers.PrimaryKeyRelatedField(queryset=Product.objects), write_only=True
    )

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
    
    def create(self, data: Dict):
        products_data = data.pop('products')
        purchase = PurchaseOpportunity.objects.create(**data)
        if products_data:
            for product in products_data:
                purchase.products.add(product)
        return purchase

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
