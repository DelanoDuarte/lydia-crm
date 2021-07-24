from address.models import Address
from address.serializers import AddressSerializer, AddressSerializerDetails
from partner_type.models import PartnerType
from partner_type.serializers import PartnerTypeSerializer
from rest_framework import serializers

from partner.models import Partner


class PartnerSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    firstName = serializers.CharField(max_length=256)
    lastName = serializers.CharField(max_length=256)
    birthDate = serializers.DateField(required=False)
    age = serializers.IntegerField(required=False)
    mobile = serializers.CharField(max_length=64, required=False)
    phone = serializers.CharField(max_length=64, required=False)
    email = serializers.CharField(max_length=128)
    firstContactDate = serializers.DateTimeField(required=False)
    comments = serializers.CharField(max_length=2048, required=False)

    full_name = serializers.CharField(read_only=True)
    get_absolute_url = serializers.CharField(read_only=True,)

    partnerType = serializers.PrimaryKeyRelatedField(queryset=PartnerType.objects)
    address = AddressSerializer()

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        if address_data:
            address = Address.objects.create(**address_data)
            return Partner.objects.create(address=address, **validated_data)

        return Partner.objects.create(**validated_data)

class PartnerListSerializer(serializers.ModelSerializer):

    partnerType = PartnerTypeSerializer()
    address = AddressSerializerDetails()

    class Meta:
        model = Partner
        fields=(
            'id',
            'firstName',
            'lastName',
            'birthDate',
            'age',
            'mobile',
            'phone',
            'email',
            'firstContactDate',
            'comments',
            'full_name',
            'partnerType',
            'address'
        )
