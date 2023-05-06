from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from apps.users.models import User
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        vd = serializer.validated_data
        phone_number = vd['phone_number']
        password = vd['password']
        first_name = vd['first_name']
        last_name = vd['last_name']
        gender = vd['gender']

        user = User.objects.update_or_create(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            is_deleted=False
        )
        print(user)
        user[0].set_password(password)

        user[0].save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ['UserRegisterAPIView']
