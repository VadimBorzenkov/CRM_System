import uuid
from datetime import timedelta
from typing import Any

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.utils.timezone import now

from users.models import User


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
    age = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите ваш возраст',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'phone', 'age')


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
