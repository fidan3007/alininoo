from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
app_name = 'accounts'

urlpatterns = [
    path('login/', Login.as_view(),name = 'login'),
    path('sign/', Register.as_view(),name = 'sign'),
    path('logout/',LogoutView.as_view(),name='logout'),
]