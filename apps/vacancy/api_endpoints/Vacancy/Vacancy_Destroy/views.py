from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.vacancy.models import Vacancy


class VacancyDestroyAPIView(DestroyAPIView):
    queryset = Vacancy.objects.all()
    permission_classes = [IsAuthenticated]


__all__ = ["VacancyDestroyAPIView"]
