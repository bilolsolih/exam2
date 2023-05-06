from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import BaseModel
from .choices import SALARY_TYPES


class Vacancy(BaseModel):
    title = models.CharField(max_length=128)

    salary_type = models.CharField(choices=SALARY_TYPES, default='f')

    salary = models.DecimalField(max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    salary_from = models.DecimalField(max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    salary_to = models.DecimalField(max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def clean(self):
        if self.salary_type == 'f' and self.salary_from:
            raise ValidationError('Salary type is fixed but the range is provided!')
        elif self.salary_type == 'f' and self.salary_to:
            raise ValidationError('Salary type is fixed but the range is provided!')
        elif self.salary_type == 'r' and self.salary:
            raise ValidationError('Salary type is ranging but fixed salary is provided!')
        elif self.salary_from >= self.salary_to and self.salary_from != 0:
            raise ValidationError('Salary from is equal to Salary to!')
        super().clean()

    def __str__(self):
        return f"Vacancy {self.title}"

# Create your models here.
