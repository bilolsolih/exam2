from rest_framework import serializers


class PhoneNumberCheckSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=128)
