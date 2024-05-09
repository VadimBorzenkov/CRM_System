import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.db.models import Q
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from customers.forms import EditCustomerForm, SearchForm, AddCustomerForm
from customers.models import Customer


def customerView(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customers.html', {'customers': customers})


class AddCustomerView(LoginRequiredMixin, View):
    template_name = 'customers/add_customer.html'
    success_url = 'customers:customers'

    def get(self, request):
        form = AddCustomerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            # Создание нового клиента с пользователем из сессии
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class EditCustomerView(UpdateView):
    template_name = 'customers/edit_customer.html'
    model = Customer
    form_class = EditCustomerForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('customers:customers')

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, pk=self.kwargs['pk'])


def delete_customer(request, pk):
    record = Customer.objects.get(pk=pk)
    record.delete()
    return redirect('customers:customers')


class SearchCustomerView(View):
    template_name = 'customers/customers.html'
    results_template_name = 'customers/customers_search_result.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)

        if form.is_valid():
            search_query = form.cleaned_data.get("name")

            # Фильтруем объекты модели Customer поиском по нескольким полям
            search_results = Customer.objects.filter(
                Q(name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(industry__icontains=search_query)
            )

            if not search_results.exists():
                return render(request, self.results_template_name, {'no_results': True})

            return render(request, self.results_template_name, {'results': search_results})

        return render(request, self.template_name, {'form': form})
