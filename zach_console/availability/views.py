# availability/views.py
from django.shortcuts import render

def pt_availability_view(request):
    return render(request, 'availability.html')