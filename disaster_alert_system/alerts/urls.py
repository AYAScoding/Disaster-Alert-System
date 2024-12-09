from django.urls import path
from . import views

app_name = 'alerts'

urlpatterns = [
    path('', views.homeAlert, name='homeAlerts'),  # Homepage for alerts
    path('create/', views.create_alert, name='createAlert'),
]




'''
urlpatterns = [
    path("alerts/", views.alert_list, name="alert_list"),
    path("alerts/<int:alert_id>/", views.alert_detail, name="alert_detail"),
    path("alerts/create/", views.create_alert, name="create_alert"),
    path("alerts/<int:alert_id>/update/", views.update_alert, name="update_alert"),
    path("alerts/<int:alert_id>/delete/", views.delete_alert, name="delete_alert"),
    path('dashboard/', views.dashboard, name='dashboard'),
]
'''