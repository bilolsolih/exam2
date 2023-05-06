from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from . import verify
from .serializers import PhoneNumberSerializer


class SendCode(APIView):
    @swagger_auto_schema(request_body=PhoneNumberSerializer)
    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        number = serializer.validated_data['number']
        print(number)
        verify.send(number)
