# zach_console/authentication/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        # Check if the email ends with '@tamu.edu'
        email = sociallogin.user.email
        if email and not email.lower().endswith('@tamu.edu'):
            # You can render a custom error page or redirect
            # For simplicity, we'll render a basic error for now
            return render(request, 'tamu_email_required.html', {'email': email})
        return True

    def pre_social_login(self, request, sociallogin):
        # This hook is called just after a user successfully authenticates via a social provider,
        # but before the login is actually processed.
        # It's another place to perform checks, and raise ImmediateHttpResponse to stop the flow.
        email = sociallogin.user.email
        if email and not email.lower().endswith('@tamu.edu'):
            # You can render a custom error page or redirect here
            # For this example, we'll raise an ImmediateHttpResponse to stop the login.
            # You might want to redirect to a more user-friendly error page.
            raise ImmediateHttpResponse(render(request, 'tamu_email_required.html', {'email': email}))