from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView


from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/signUp.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляю! Вы успешно зарегистрировались!'
    title = 'RelaTech - Регистрация'


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/signIn.html'
    form_class = UserLoginForm
    title = 'RelaTech - Авторизация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Store - Личный кабинет'

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', args=(self.object.id,))
