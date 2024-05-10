from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from deals.models import Deal, Product
from deals.forms import AddDealForm, AddProductForm, EditDealForm, SearchForm


class IndexView(TemplateView):
    template_name = 'deals/index.html'
    title = 'RelaTech'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Если пользователь аутентифицирован, получаем его тип
            user_type = self.request.user.user_type
            context['user_type'] = user_type
        return context


def dealView(request):
    deals = Deal.objects.all()

    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, получаем его тип
        user_type = request.user.user_type
    else:
        # Если пользователь не аутентифицирован, устанавливаем тип по умолчанию
        user_type = None

    # Добавляем тип пользователя в контекст
    context = {'deals': deals, 'user_type': user_type}

    return render(request, 'deals/deals.html', context)


# def productView(request):
#     products = Product.objects.all()
#     return render(request, 'deals/products.html', {'products': products})


class AddDealView(LoginRequiredMixin, View):
    template_name = 'deals/add_deal.html'
    success_url = 'deals:deals'

    def get(self, request):
        form = AddDealForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddDealForm(request.POST)
        if form.is_valid():
            # Получение текущего клиента из сессии
            # получаем первого клиента пользователя
            customer = request.user

            if customer:
                # Создание новой сделки с указанием текущего клиента
                deal = form.save(commit=False)
                deal.customer = customer  # изменение на customer
                deal.save()

                return redirect(self.success_url)
            else:
                # Обработка ситуации, если пользователь не связан с клиентом
                pass

        return render(request, self.template_name, {'form': form})


class AddPoductView(View):
    template_name = 'deals/add_product.html'
    success_url = 'deals:deals'

    def get(self, request):
        form = AddProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class EditDealView(UpdateView):
    template_name = 'deals/edit_deal.html'
    model = Deal
    form_class = EditDealForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('deals:deals')

    def get_object(self, queryset=None):
        return get_object_or_404(Deal, pk=self.kwargs['pk'])


def delete_deal(request, pk):
    record = Deal.objects.get(pk=pk)
    record.delete()
    return redirect('deals:deals')


class SearchDealView(View):
    template_name = 'deals/deals.html'
    results_template_name = 'deals/deals_search_result.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)

        if form.is_valid():
            search_query = form.cleaned_data.get("customer")

            # Фильтруем объекты модели Deal поиском по полю customer
            search_results = Deal.objects.filter(
                customer__name__icontains=search_query)

            if not search_results.exists():
                return render(request, self.results_template_name, {'no_results': True})

            return render(request, self.results_template_name, {'results': search_results, 'form': form})

        return render(request, self.template_name, {'form': form})
