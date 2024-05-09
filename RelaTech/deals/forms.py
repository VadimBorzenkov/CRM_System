from django import forms

from deals.models import Deal, Product


class AddDealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['product', 'quantity', 'unit_price']
        labels = {
            'product': 'Продукт',
            'quantity': 'Количество',
            'unit_price': 'Цена за единицу',
        }
        widgets = {
            # Используем виджет Select для выбора продукта из списка
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']


class EditDealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['product', 'quantity', 'unit_price',
                  'total_amount', 'deal_date', 'status']
        labels = {
            'product': 'Продукт',
            'quantity': 'Количество',
            'unit_price': 'Цена за единицу',
            'total_amount': 'Общая сумма',
            'deal_date': 'Дата сделки',
            'status': 'Статус',
        }
        widgets = {
            'deal_date': forms.DateInput(attrs={'type': 'date'}),
        }

        exclude = ['deal_date']
