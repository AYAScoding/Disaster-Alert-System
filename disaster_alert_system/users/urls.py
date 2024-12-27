from django.urls import path
from . import views

app_name = 'users'  

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('landing/', views.landing_page, name='landing'),  # Default route
    path('login/', views.login_view, name='login'),  
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.edit_profile, name='edit_profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
