from unicodedata import decimal
from django.db import models

from accounts.models import User
from menu.models import FoodItem


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user


class Tax(models.Model):
    tax_type = models.CharField(max_length=20, unique=True, verbose_name='Tipo de impuesto')
    tax_percentage = models.DecimalField(max_digits=4, decimal_places=2, max_length=4, verbose_name='Porcentaje de impuesto (%)')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Impuesto'
        verbose_name_plural = 'Impuestos'

    def __str__(self):
        return self.tax_type
