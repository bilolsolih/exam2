from django.db import models

from apps.common.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=24, decimal_places=2, default=0)
    marja = models.DecimalField(max_digits=24, decimal_places=2, default=0)
    package_code = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
