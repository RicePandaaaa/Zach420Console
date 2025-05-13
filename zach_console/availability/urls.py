# availability/urls.py
from django.urls import path
from . import views

app_name = 'availability'  # Application namespace

urlpatterns = [
    path('', views.pt_availability_view, name='pt_availability_page'),
]