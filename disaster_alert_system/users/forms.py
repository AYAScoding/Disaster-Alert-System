from django.db import transaction
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from captcha.fields import CaptchaField

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()  # Add CAPTCHA to the login form

# Define the choices for the location dropdown
LOCATION_CHOICES = [
    ('Girne', 'Girne'),
    ('Lefkoşa', 'Lefkoşa'),
    ('Lefke', 'Lefke'),
    ('İskel', 'İskele'),
    ('Gazimağusa', 'Gazimağusa'),
    ('Güzelyurt', 'Güzelyurt'),
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.IntegerField( required=True, help_text="Enter your phone number.")
    location = forms.ChoiceField(choices=LOCATION_CHOICES, required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'required'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'required'})
    )

   

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'location', 'password1', 'password2']

     



    @transaction.atomic
    def save(self, commit=True):
        # Save the user instance first
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        # Safely access the phone and location fields
        phone = self.cleaned_data.get('phone')
        location = self.cleaned_data.get('location')

        # Ensure values are provided before saving the profile
        if phone is None or location is None:
            raise ValueError("Phone and location must be provided.")

        # Check if a profile already exists for the user, if so, update it
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={'phone': phone, 'location': location}
        )

        # If the profile was created, return the user
        if created:
            return user
        
        # If the profile already exists, just update the phone and location
        profile.phone = phone
        profile.location = location
        profile.save()

        return user
    

    
    