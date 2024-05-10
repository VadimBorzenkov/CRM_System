from django.db import models

from users.models import User


class Customer(models.Model):
    ORGANIZATION_CHOICES = [
        ('ООО', 'ООО'),
        ('ИП', 'ИП'),
        ('Физическое лицо', 'Физическое лицо'),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customers')
    organization = models.CharField(
        max_length=20, verbose_name='Организация', choices=ORGANIZATION_CHOICES, default='Физическое лицо')
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(
        max_length=20, verbose_name='Телефон', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес', blank=True, null=True)
    industry = models.CharField(
        max_length=100, verbose_name='Отрасль', blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name
