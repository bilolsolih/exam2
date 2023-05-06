from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.product.renderers import CustomAesRenderer
from .serializers import ProductListSerializer
from ....models import Product


class ProductListEncryptedView(APIView):
    renderer_classes = [CustomAesRenderer]

    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProductListSerializer(products, many=True)
            data = serializer.data
            data = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'data': data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'No product is available'})
