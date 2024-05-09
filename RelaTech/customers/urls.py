from django.urls import include, path

from customers.views import customerView, AddCustomerView, EditCustomerView, delete_customer, SearchCustomerView


app_name = 'customers'

urlpatterns = [
    path('', customerView, name='customers'),
    path('add/', AddCustomerView.as_view(), name='add_customer'),
    path('edit/<int:pk>/', EditCustomerView.as_view(), name='edit_customer'),
    path('delete/<int:pk>/', delete_customer, name='delete_customer'),
    path('search/', SearchCustomerView.as_view(), name='customers_search'),
    path('search/result', SearchCustomerView.as_view(template_name='customers_search_result.html'),
         name='search_result'),


]
