from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from users.views import UserRegistrationView, UserLoginView, UserProfileView, CompanyRegistrationView, ChoiceView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('choice/', ChoiceView.as_view(), name='choice'),
    path('user_registration/', UserRegistrationView.as_view(),
         name='user_registration'),
    path('company_registration/', CompanyRegistrationView.as_view(),
         name='company_registration'),
    path('profile/<int:pk>/',
         login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
