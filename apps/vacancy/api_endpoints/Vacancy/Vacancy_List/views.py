from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import VacancyListSerializer
from ....models import Vacancy


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer

    # def get(self, request, salary=None, *args, **kwargs):
    #     self.queryset = Vacancy.objects.all()
    #     if salary:
    #         set1 = self.queryset.filter(salary__gte=salary)
    #         set2 = self.queryset.filter(salary_from__gte=salary)
    #         serializer1 = VacancyListSerializer(set1)
    #         serializer2 = VacancyListSerializer(set1)
    #         return Response(serializer1.data + serializer2.data)
    #     serializer = VacancyListSerializer(self.queryset)
    #     return Response(serializer.data)


__all__ = ["VacancyListAPIView"]
