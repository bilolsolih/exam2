from rest_framework import filters
from rest_framework.generics import ListAPIView

from .serializers import VacancyListSerializer
from ....models import Vacancy


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['salary', 'salary_from', 'salary_to']


__all__ = ["VacancyListAPIView"]
