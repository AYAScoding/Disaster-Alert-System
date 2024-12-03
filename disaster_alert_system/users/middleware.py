from django.shortcuts import redirect
from django.urls import reverse

class SessionValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip session validation for public paths (e.g., login, register)
        public_paths = [reverse('users:login'), reverse('users:register')]
        if 'user_id' not in request.session and request.path not in public_paths:
            return redirect('users:login')
        return self.get_response(request)
