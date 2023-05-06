from rest_framework.generics import DestroyAPIView

from apps.users.models import User
from .permissions import IsTheSameUser


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [IsTheSameUser]
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.phone_number = None
        instance.save()


__all__ = ['UserDestroyAPIView']
