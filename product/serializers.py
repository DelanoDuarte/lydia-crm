
from typing import Dict, Tuple

from product_category.models import ProductCategory
from product_category.serializers import ProductCategorySerializer
from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    unit_price = serializers.FloatField(required=True)
    active = serializers.BooleanField(required=False)
    
    # relationships
    product_category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects)
    #product_category = ProductCategorySerializer(read_only=True, many=False)

    def create(self, validated_data: Dict):
        return Product.objects.create(**validated_data)


class ProductListSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer()
    
    class Meta:
        model = Product
        fields=(
            '__all__'
        )
