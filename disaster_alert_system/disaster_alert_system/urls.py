from django.contrib import admin
from django.urls import path, include
from users import views as user_views  # Importing the views from users app
from alerts import views as alerts_views  # Importing the views from alerts app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Handles login, logout, etc.
    path('alerts/', include('alerts.urls')),  # Includes all alert-related URLs
    path('', user_views.login_view, name='login'),
    path('users/', include('users.urls')),  # Make sure this is correct
]
