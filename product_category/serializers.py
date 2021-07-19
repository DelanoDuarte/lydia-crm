from product_category.models import ProductCategory
from rest_framework import serializers

class ProductCategorySerializer(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=2048, required=False)
    active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return ProductCategory.objects.create(**validated_data)