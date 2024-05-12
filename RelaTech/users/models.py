from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('user', 'Обычный пользователь'),
        ('company', 'Фирма'),
        ('admin', 'Администратор'),
    ]
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default='user')
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    photo = models.ImageField(upload_to='users_photos', blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

