from django.urls import path

from apps.verify.api_endpoints.Verify_Check.views import CheckCode
from apps.verify.api_endpoints.Verify_Send.views import SendCode

app_name = 'verify'

urlpatterns = [
    path('verify/send/', SendCode.as_view(), name='verify_send'),
    path('verify/check/', CheckCode.as_view(), name='verify_check'),
]
