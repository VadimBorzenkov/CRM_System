from django.urls import include, path

from deals.views import dealView, AddDealView, AddPoductView, EditDealView, delete_deal, SearchDealView

app_name = 'deals'

urlpatterns = [
    path('', dealView, name='deals'),
    path('add_deal/', AddDealView.as_view(), name='add_deal'),
    path('add_product/', AddPoductView.as_view(), name='add_product'),
    path('edit_deal/<int:pk>', EditDealView.as_view(), name='edit_deal'),
    path('delete/<int:pk>/', delete_deal, name='delete_deal'),
    path('search/', SearchDealView.as_view(), name='deals_search'),
    path('search/result', SearchDealView.as_view(template_name='deals_search_result.html'),
         name='deals_search_result'),



]
