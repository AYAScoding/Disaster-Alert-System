from django.db import models
from django.contrib.auth.models import User
from users.models import Profile  # Import the Profile model

class DisasterAlert(models.Model):
    ALERT_TYPES = [
        ('Earthquake', 'Earthquake'),
        ('Flood', 'Flood'),
        ('Wild Fire', 'Wild Fire'),
        ('Tsunami', 'Tsunami'),
    ]

    type = models.CharField(max_length=50, choices=ALERT_TYPES)
    description = models.TextField()
    location = models.CharField(
        max_length=50,
        choices=Profile.LOCATION_CHOICES,  # Use Profile location choices
        blank=False,
        null=False
    )
    severity = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_issued = models.DateTimeField()

    def __str__(self):
        return f'{self.type} Alert - {self.location}'
