from django.db import models

from users.models import User
from customers.models import Customer
from companies.models import Product, Company


class Deal(models.Model):
    STATUS_CHOICES = [
        ('1', 'Создана'),
        ('2', 'В обработке'),
        ('3', 'Завершена'),
    ]
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='deals')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='deals', default=None, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Общая сумма')
    deal_date = models.DateField(verbose_name='Дата сделки', auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='1')

    def save(self, *args, **kwargs):
        # Рассчитываем общую сумму сделки перед сохранением объекта
        self.total_amount = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.deal_date}"

    def update_status(self, new_status):
        self.status = new_status
        self.save()
