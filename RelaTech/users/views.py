from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model


from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, CompanyRegistrationForm
from users.models import User
from deals.models import Deal
from customers.models import Customer
from companies.models import Company, Product


class ChoiceView(TemplateView, TitleMixin):
    template_name = 'users/user_or_company.html'
    title = "Регистрация"


class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name = 'users/user_signup.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляю! Вы успешно зарегистрировались!'
    title = 'RelaTech - Регистрация'

    def form_valid(self, form):
        return super().form_valid(form)


class CompanyRegistrationView(CreateView):
    model = get_user_model()
    form_class = CompanyRegistrationForm
    template_name = 'users/company_signup.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Ваша компания успешно зарегистрирована!'
    title = 'Регистрация компании'

    def form_valid(self, form):
        # Вызываем метод save формы, чтобы создать пользователя и компанию
        user = form.save()
        return super().form_valid(form)


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
        user_company = user.company if hasattr(user, 'company') else None
        if user_company:
            company_products = Product.objects.filter(company=user_company)
            context['company_products'] = company_products
        context['user_deals'] = user_deals
        context['user_customers'] = user_customers
        return context
