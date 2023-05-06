from rest_framework import serializers


class PhoneNumberSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=20)
