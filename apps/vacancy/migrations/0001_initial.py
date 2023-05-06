# Generated by Django 4.2.1 on 2023-05-06 09:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('salary_type', models.CharField(choices=[('r', 'Ranging salary'), ('f', 'Fixed salary')], default='f')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=24, validators=[django.core.validators.MinValueValidator(0)])),
                ('salary_from', models.DecimalField(decimal_places=2, default=0, max_digits=24, validators=[django.core.validators.MinValueValidator(0)])),
                ('salary_to', models.DecimalField(decimal_places=2, default=0, max_digits=24, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
    ]
