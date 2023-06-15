from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.login, name='login'), #ok
    path('cadastro', views.cadastro, name='cadastro'), #ok
    path('dash', views.dash, name='dash'), #ok





]