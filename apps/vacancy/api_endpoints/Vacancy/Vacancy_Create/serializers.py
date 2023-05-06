from rest_framework.serializers import ModelSerializer

from apps.vacancy.models import Vacancy


class VacancyCreateSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
