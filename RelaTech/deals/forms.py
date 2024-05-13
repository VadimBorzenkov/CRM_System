from django import forms

from deals.models import Deal, Product
from customers.models import Customer


class AddDealForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Customer.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            if user.user_type == 'company':
                # Показываем всех пользователей для компании
                self.fields['client'].queryset = Customer.objects.all()
                # Ограничиваем выбор продуктов только для текущей компании
                self.fields['product'].queryset = Product.objects.filter(
                    company=user.company)
            elif user.user_type == 'admin':
                # Показываем всех клиентов и все продукты для админа
                self.fields['client'].queryset = Customer.objects.all()
                self.fields['product'].queryset = Product.objects.all()

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
