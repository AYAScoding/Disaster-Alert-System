from django.db import transaction
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator

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
    location = forms.ChoiceField(choices=LOCATION_CHOICES, required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'required'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'required'})
    )

   

    class Meta:
        model = User
        fields = ['username', 'email', 'location', 'password1', 'password2']

     



    from django.db import transaction
from .models import Profile

@transaction.atomic
def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']

    if commit:
        user.save()

    # Get the location value from the form
    location = self.cleaned_data.get('location')

    # Validate location before saving the profile
    if not location:
        raise ValueError("Location field is required.")

    # Use update_or_create to avoid duplicate profiles, only with location
    Profile.objects.update_or_create(
        user=user,
        defaults={'location': location}
    )

    return user
