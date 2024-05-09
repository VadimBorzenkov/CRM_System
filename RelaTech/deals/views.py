from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from deals.models import Deal, Product
from deals.forms import AddDealForm, AddProductForm, EditDealForm


def dealView(request):
    deals = Deal.objects.all()
    return render(request, 'deals/deals.html', {'deals': deals})


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
            # Создание новой сделки с пользователем из сессии
            deal = form.save(commit=False)
            deal.user = request.user
            deal.save()
            return redirect(self.success_url)
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
