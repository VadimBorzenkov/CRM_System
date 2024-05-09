from django import forms

from customers.models import Customer


class EditCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['organization', 'name', 'email',
                  'phone', 'address', 'industry']


class SearchForm(forms.Form):
    name = forms.CharField(
        label='Поиск по названию организации',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название организации'})
    )


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['organization', 'name', 'email',
                  'phone', 'address', 'industry']
        widgets = {
            'organization': forms.Select(choices=Customer.ORGANIZATION_CHOICES, attrs={'class': 'form-control'}),
        }
