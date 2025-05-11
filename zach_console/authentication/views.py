from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

def custom_login_page_view(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'login_page.html')