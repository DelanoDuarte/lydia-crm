from .models import Address
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):

    mainAddress = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    country = serializers.CharField(required=False)

    class Meta:
        model = Address
        fields = (
            'mainAddress',
            'additionalAddress',
            'state',
            'city',
            'country'
        )
    
    def create(self, validated_data):
        return Address.objects.create(**validated_data)

class AddressSerializerDetails(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            '__all__'
        )