from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField




class Profile(models.Model):
    LOCATION_CHOICES = [
            ('Girne', 'Girne'),
            ('Lefkoşa', 'Lefkoşa'),
            ('Lefke', 'Lefke'),
            ('İskel', 'İskele'),
            ('Gazimağusa', 'Gazimağusa'),
            ('Güzelyurt', 'Güzelyurt'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, blank=True , null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
