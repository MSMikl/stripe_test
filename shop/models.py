from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Item(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=100,
    )
    description = models.TextField(
        'Описание продукта',
        blank=True,
    )
    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
