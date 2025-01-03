from django.urls import path
from . import views

app_name = 'alerts'

urlpatterns = [
    path('', views.homeAlert, name='homeAlerts'),  # Homepage for alerts
   
    path('add/', views.add_alert, name='add_alert'),
    path('edit/<int:alert_id>/', views.edit_alert, name='edit_alert'),
    path('delete/<int:alert_id>/', views.delete_alert, name='delete_alert'),

]




