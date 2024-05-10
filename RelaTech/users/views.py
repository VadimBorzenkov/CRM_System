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
from deals.models import Deal
from customers.models import Customer


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
    title = 'RelaTech - Личный кабинет'

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        user_deals = Deal.objects.filter(customer=user)
        user_customers = Customer.objects.filter(user=user)
        context['user_deals'] = user_deals
        context['user_customers'] = user_customers

        return context
