from django import forms

from companies.models import Product, Company


class AddProductForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание', widget=forms.Textarea, required=False)

    class Meta:
        model = Product
        fields = ['company', 'name', 'description', 'price']


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['company', 'name', 'description', 'price',]
        labels = {
            'company': 'Компания',
            'name': 'Продукт',
            'description': 'Описание',
            'price': 'Цена',
        }


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'user',]


class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'user',]
        labels = {
            'name': 'Компания',
            'user': 'Держатель',
        }
