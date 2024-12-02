from django.db import models
from django.contrib.auth.models import User
from alerts.models import DisasterAlert

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alert = models.ForeignKey(DisasterAlert, on_delete=models.CASCADE)
    notified_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} about {self.alert.alert_type}"
