from django.urls import path

from apps.users.api_endpoints.User.User_Destroy.views import UserDestroyAPIView
from apps.users.api_endpoints.User.User_Login.views import LoginAPIView
from apps.users.api_endpoints.User.User_Register.views import UserRegisterAPIView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('delete-user/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]
