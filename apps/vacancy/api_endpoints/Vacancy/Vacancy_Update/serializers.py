from rest_framework import serializers

from apps.vacancy.models import Vacancy


class VacancyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
