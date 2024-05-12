from django.urls import include, path

from deals.views import dealView, AddDealView, EditDealView, delete_deal, SearchDealView, UpdateDealStatusView

app_name = 'deals'

urlpatterns = [
    path('', dealView, name='deals'),
    path('add_deal/', AddDealView.as_view(), name='add_deal'),
    path('update_deal_status/<int:pk>',
         UpdateDealStatusView.as_view(), name='update_deal_status'),

    path('edit_deal/<int:pk>', EditDealView.as_view(), name='edit_deal'),
    path('delete/<int:pk>/', delete_deal, name='delete_deal'),
    path('search/', SearchDealView.as_view(), name='deals_search'),
    path('search/result', SearchDealView.as_view(template_name='deals_search_result.html'),
         name='deals_search_result'),



]
