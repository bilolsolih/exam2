from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser

from apps.vacancy.models import Vacancy
from .serializers import VacancyUpdateSerializer


class VacancyUpdateAPIView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer
    parser_classes = [FormParser]


__all__ = ["VacancyUpdateAPIView"]
