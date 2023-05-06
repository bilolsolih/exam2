from rest_framework import serializers

from apps.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'profile_photo', 'password', 'gender']

    def validate_phone_number(self, value):
        return value
