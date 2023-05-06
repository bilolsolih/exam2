from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from apps.vacancy.models import Vacancy
from .serializers import VacancyCreateSerializer


class VacancyCreateAPIView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser]


__all__ = ["VacancyCreateAPIView"]
