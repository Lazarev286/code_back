from django.urls import path
from django.contrib.auth import login, logout
from django.contrib.auth.views import  logout_then_login

from . import views


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('', views.dashboard, name='dashboard'),
]