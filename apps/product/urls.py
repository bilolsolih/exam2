from django.urls import path

from apps.product.api_endpoints.Product.Product_List.views import ProductListEncryptedView

app_name = 'product'

urlpatterns = [
    path('products/', ProductListEncryptedView.as_view(), name='product_list')
]
