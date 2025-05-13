# mywebsite/mywebsite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('app/', include('authentication.urls')),
    path('availability/', include('availability.urls')),
]