import uuid
from datetime import timedelta
from typing import Any

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.utils.timezone import now
from django.contrib.auth import get_user_model

from users.models import User
from companies.models import Company
from customers.models import Customer


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    organization = forms.ChoiceField(
        choices=Customer.ORGANIZATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control py-4',
        }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите номер телефона',
    }))

    class Meta:
        model = get_user_model()
        fields = ('organization', 'first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'phone',)

    def save(self, commit=True):
        user = super().save(commit=False)
        # Добавьте логику для создания записи в таблице Customer
        # Используйте данные из формы для создания объекта Customer
        if commit:
            user.save()

            Customer.objects.create(user=user,
                                    organization=self.cleaned_data['organization'],
                                    name=self.cleaned_data['username'],
                                    email=self.cleaned_data['email'],
                                    phone=self.cleaned_data['phone']
                                    )
        return user


class CompanyRegistrationForm(forms.ModelForm):
    user_type = forms.CharField(
        widget=forms.HiddenInput(), initial='company', required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль',
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Название компании',
    }))

    class Meta:
        model = get_user_model()
        fields = ['user_type', 'username', 'email',
                  'password1', 'password2', 'name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'company'
        password1 = self.cleaned_data.get('password1')
        if password1:
            # Если пароль был введен, задаем его
            user.set_password(password1)
        if commit:
            user.save()
            name = self.cleaned_data['name']
            # Проверяем, существует ли компания для пользователя
            if not hasattr(user, 'company'):
                Company.objects.create(user=user, name=name)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
