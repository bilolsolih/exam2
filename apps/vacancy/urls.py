from django.urls import path

from apps.vacancy.api_endpoints.Vacancy.Vacancy_List.views import VacancyListAPIView

app_name = 'vacancy'

urlpatterns = [
    path('vacancy/', VacancyListAPIView.as_view(), name='vacancy_list'),
    path('vacancy/<int:salary>/', VacancyListAPIView.as_view(), name='vacancy_list_by_salary'),
]
