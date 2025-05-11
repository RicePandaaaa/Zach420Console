# core/urls.py
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.custom_login_page_view, name='custom_login_page'),

]