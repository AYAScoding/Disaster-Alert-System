from django.contrib import admin
from django.urls import path, include
from users import views as user_views  # Importing the views from users app
from alerts import views as alerts_views  # Importing the views from alerts app
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Handles login, logout, etc.
    path('alerts/', include('alerts.urls')),  # Includes all alert-related URLs
    path('', RedirectView.as_view(url=reverse_lazy('users:landing')), name='root'),
    path('users/', include('users.urls')),  # Make sure this is correct
    path('captcha/', include('captcha.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



