from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from . import verify
from .serializers import PhoneNumberCheckSerializer


class CheckCode(APIView):
    @swagger_auto_schema(request_body=PhoneNumberCheckSerializer)
    def post(self, request):
        serializer = PhoneNumberCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        number = serializer.validated_data['number']
        code = serializer.validated_data['code']
        if verify.check(number, code):
            return Response({'status': 'Verified successfully'})
        else:
            return Response({'status': 'Not verified successfully'})
