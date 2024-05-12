from django import forms

from deals.models import Deal, Product
from customers.models import Customer


class AddDealForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Customer.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated and user.user_type == 'company':
            # Показываем всех пользователей
            self.fields['client'].queryset = Customer.objects.all()

    class Meta:
        model = Deal
        fields = ['product', 'quantity', 'client']


class EditDealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['product', 'quantity',
                  'total_amount', 'deal_date', 'status']
        labels = {
            'product': 'Продукт',
            'quantity': 'Количество',
            'total_amount': 'Общая сумма',
            'deal_date': 'Дата сделки',
            'status': 'Статус',
        }
        widgets = {
            'deal_date': forms.DateInput(attrs={'type': 'date'}),
        }

        exclude = ['deal_date']


class SearchForm(forms.Form):
    name = forms.CharField(
        label='Поиск по клиенту',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите клиента'})
    )
