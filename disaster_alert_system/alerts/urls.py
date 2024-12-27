from django.urls import path
from . import views

app_name = 'alerts'

urlpatterns = [
    path('', views.homeAlert, name='homeAlerts'),  # Homepage for alerts
    path('create/', views.create_alert, name='createAlert'),
]




