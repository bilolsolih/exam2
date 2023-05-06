from rest_framework.serializers import ModelSerializer

from ....models import Product


class ProductRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'marja', 'package_code']
