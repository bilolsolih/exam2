from rest_framework.serializers import ModelSerializer

from apps.vacancy.models import Vacancy


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'salary_from', 'salary_to']
