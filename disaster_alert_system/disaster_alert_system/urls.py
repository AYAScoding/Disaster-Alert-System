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
# password reset
     path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),
     

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

