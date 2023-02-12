from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField()
    house_number = serializers.CharField()
    city = serializers.CharField()
    zip_code = serializers.CharField()


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(source="name")
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    sex = serializers.CharField()
    addresses = AddressSerializer(many=True)
