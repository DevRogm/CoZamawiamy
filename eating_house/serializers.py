from rest_framework import serializers

from eating_house.models import EatingHouse, Address


class AddressSerializer(serializers.ModelSerializer):
    apartment_number = serializers.CharField(required=False, allow_null=True, allow_blank=True, default=None)

    class Meta:
        model = Address
        fields = ["country", "city", "street", "street_number", "apartment_number", "postal_code"]

class EatingHouseSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = EatingHouse
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        eating_house = EatingHouse.objects.create(address=address, **validated_data)
        return eating_house