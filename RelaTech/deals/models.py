from django.db import models

from users.models import User
from customers.models import Customer


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Deal(models.Model):
    STATUS_CHOICES = [
        ('1', 'Создана'),
        ('2', 'В обработке'),
        ('3', 'Завершена'),
    ]
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Общая сумма')
    deal_date = models.DateField(verbose_name='Дата сделки', auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='1')

    def save(self, *args, **kwargs):
        # Рассчитываем общую сумму сделки перед сохранением объекта
        self.total_amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.deal_date}"
