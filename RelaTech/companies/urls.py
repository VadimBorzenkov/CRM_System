from django.urls import include, path

from companies.views import productView, AddPoductView, EditProductView, delete_product, companyView, AddCompanyView, EditCompanyView, delete_company

app_name = 'companies'

urlpatterns = [
    path('', companyView, name='companies'),
    path('add_company', AddCompanyView.as_view(), name='add_company'),
    path('edit_company/<int:pk>', EditCompanyView.as_view(), name='edit_company'),
    path('delete_company/<int:pk>', delete_company, name='delete_company'),

    path('products/', productView, name='products'),
    path('add_product/', AddPoductView.as_view(), name='add_product'),
    path('edit_product/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),

]
