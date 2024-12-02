from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    LOCATION_CHOICES = [
            ('girne', 'Girne'),
            ('lefkoşa', 'Lefkoşa'),
            ('lefke', 'Lefke'),
            ('iskele', 'İskele'),
            ('gazimağusa', 'Gazimağusa'),
            ('güzelyurt', 'Güzelyurt'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True , null=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, blank=True , null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
