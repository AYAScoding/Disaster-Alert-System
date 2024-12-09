from django.shortcuts import redirect
from django.urls import reverse

class SessionValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define public paths that don't require authentication
        public_paths = [
            reverse('users:login'),
            reverse('users:register'),
            reverse('users:landing'),  # Include the landing page
        ]

        # Allow access to public paths without session validation
        if request.path not in public_paths and 'user_id' not in request.session:
            return redirect('users:login')

        return self.get_response(request)
