# zach_console/authentication/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        # Check if the email ends with '@tamu.edu'
        email = sociallogin.user.email
        if email and not email.lower().endswith('@tamu.edu'):
            return False
        return True

    def pre_social_login(self, request, sociallogin):
        # This hook is called just after a user successfully authenticates via a social provider,
        # but before the login is actually processed.
        email = sociallogin.user.email
        if email and not email.lower().endswith('@tamu.edu'):
            # Add error message and redirect back to login page
            messages.error(
                request, 
                f'Access denied. The email address "{email}" is not a valid TAMU email address. '
                f'Only emails ending with "@tamu.edu" are allowed to sign in as Peer Teachers.'
            )
            raise ImmediateHttpResponse(redirect(reverse('authentication:custom_login_page')))