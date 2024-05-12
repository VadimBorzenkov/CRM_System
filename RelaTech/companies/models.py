from django.db import models

from users.models import User


class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='company', verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='Название фирмы')

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='products', verbose_name='Фирма')
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
