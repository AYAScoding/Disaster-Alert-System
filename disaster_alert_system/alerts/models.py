from django.db import models
from django.contrib.auth.models import User
from users.models import Profile  # Import the Profile model
import uuid

class DisasterAlert(models.Model):
    ALERT_TYPES = [
    ('Earthquake', 'Earthquake'),
    ('Flood', 'Flood'),
    ('Wild Fire', 'Wild Fire'),
    ('Tsunami', 'Tsunami'),
    ('Hurricane', 'Hurricane'),
    ('Tornado', 'Tornado'),
    ('Landslide', 'Landslide'),
    ('Drought', 'Drought'),
    ('Volcanic Eruption', 'Volcanic Eruption'),
    ('Snowstorm', 'Snowstorm'),
    ('Avalanche', 'Avalanche'),
    ('Heatwave', 'Heatwave'),
    ('Cyclone', 'Cyclone'),
    ('Blizzard', 'Blizzard'),
    ('Sandstorm', 'Sandstorm')
]
    SEVERITY_LEVELS = [
        ('High','High'),
        ('Mediem High','Mediem High'),
        ('Mediem','Mediem'),
        ('Mediem Low','Mediem Low'),
        ('Low','Low')
    ]


    type = models.CharField(max_length=50, choices=ALERT_TYPES)
    description = models.TextField()
    location = models.CharField(
        max_length=50,
        choices=Profile.LOCATION_CHOICES,  # Use Profile location choices
        blank=False,
        null=False
    )
    image = models.ImageField(upload_to='alert_images/', blank=True, null=True)  
    severity = models.CharField(max_length=50, choices=SEVERITY_LEVELS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_issued = models.DateTimeField()

    def __str__(self):
        return f'{self.type} Alert - {self.location}'
