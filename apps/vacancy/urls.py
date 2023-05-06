from django.urls import path

from apps.vacancy.api_endpoints.Vacancy.Vacancy_Create.views import VacancyCreateAPIView
from apps.vacancy.api_endpoints.Vacancy.Vacancy_Destroy.views import VacancyDestroyAPIView
from apps.vacancy.api_endpoints.Vacancy.Vacancy_List.views import VacancyListAPIView
from apps.vacancy.api_endpoints.Vacancy.Vacancy_Update.views import VacancyUpdateAPIView

app_name = 'vacancy'

urlpatterns = [
    path('vacancy/', VacancyListAPIView.as_view(), name='vacancy_list'),
    path('vacancy/<int:salary>/', VacancyListAPIView.as_view(), name='vacancy_list_by_salary'),
    path('vacancy/create/', VacancyCreateAPIView.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>/', VacancyUpdateAPIView.as_view(), name='vacancy_update'),
    path('vacancy/destroy/<int:pk>/', VacancyDestroyAPIView.as_view(), name='vacancy_destroy'),

]
