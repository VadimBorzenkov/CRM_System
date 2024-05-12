from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


from companies.forms import AddProductForm, EditProductForm, AddCompanyForm, EditCompanyForm
from companies.models import Product, Company


def productView(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, получаем его тип
        user_type = request.user.user_type
    else:
        # Если пользователь не аутентифицирован, устанавливаем тип по умолчанию
        user_type = None

    # Добавляем тип пользователя в контекст
    context = {'products': products, 'user_type': user_type}

    return render(request, 'companies/products.html', context)


class AddPoductView(View):
    template_name = 'companies/add_product.html'
    success_url = 'companies:products'

    def get(self, request):
        form = AddProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class EditProductView(UpdateView):
    template_name = 'companies/edt_product.html'
    model = Product
    form_class = EditProductForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('companies:products')

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs['pk'])


def delete_product(request, pk):
    record = Product.objects.get(pk=pk)
    record.delete()
    return redirect('companies:products')


def companyView(request):
    companies = Company.objects.all()

    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, получаем его тип
        user_type = request.user.user_type
    else:
        # Если пользователь не аутентифицирован, устанавливаем тип по умолчанию
        user_type = None

    # Добавляем тип пользователя в контекст
    context = {'companies': companies, 'user_type': user_type}

    return render(request, 'companies/companies.html', context)


class AddCompanyView(View):
    template_name = 'companies/add_company.html'
    success_url = 'companies:companies'

    def get(self, request):
        form = AddCompanyForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class EditCompanyView(UpdateView):
    template_name = 'companies/edit_company.html'
    model = Company
    form_class = EditCompanyForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('companies:companies')

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs['pk'])


def delete_company(request, pk):
    record = Company.objects.get(pk=pk)
    record.delete()
    return redirect('companies:companies')
