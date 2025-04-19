from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import DisasterAlertForm
from .models import DisasterAlert
from django.shortcuts import render, get_object_or_404, redirect


# Admin-only decorator
def admin_required(user):
    return user.is_staff  # or user.is_superuser, depending on your logic



def homeAlert(request):
    alerts = []
    if request.user.is_authenticated:
        user_location = request.user.profile.location  # Fetch user's location from their profile
        if user_location:
            alerts = DisasterAlert.objects.filter(location=user_location).order_by('-date_issued')
    return render(request, 'alerts/homeAlert.html', {'alerts': alerts})

   
   
# Add a new alert

def add_alert(request):
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST, request.FILES)
        if form.is_valid():
            alert = form.save()  # Save the alert instance
            notify_users(alert)  # Call the function to send email notifications
            return redirect('users:admin_dashboard')
    else:
        form = DisasterAlertForm()
    return render(request, 'alerts/add_alert.html', {'form': form})



from django.core.mail import send_mail
from django.contrib.auth.models import User
from users.models import Profile
from django.core.mail import EmailMultiAlternatives


def notify_users(alert):
    """
    Notify users via email when an alert is created for their location.
    """
    # Fetch profiles whose location matches the alert location
    profiles = Profile.objects.filter(location=alert.location)

    for profile in profiles:
        user = profile.user  # Get the related User instance
        if user.email:  # Ensure the user has an email address
            subject = f"New {alert.type} Alert in {alert.location}"
            message = f"""
            Dear {user.username},

            A new alert has been issued for your location:

            - Type: {alert.type}
            - Severity: {alert.severity}

            - Description: {alert.description}

            Stay safe and take all necessary precautions.

            Best regards,
            Disaster Alert System Team
            """
             # HTML version of the email
            html_content = f"""
            <html>
            <body>
                <h2 style="color: #2c3e50;">Dear {user.username},</h2>
                <p>A new alert has been issued for your location:</p>
                <ul>
                    <li><strong>Type:</strong> {alert.type}</li>
                    <li><strong>Severity:</strong> {alert.severity}</li>
                    <li><strong>Description:</strong> {alert.description}</li>
                </ul>
                <p style="color: #e74c3c;">Stay safe and take all necessary precautions.</p>
                <br>
                <p>Best regards,</p>
                <p style="font-weight: bold;">Disaster Alert System Team</p>
            </body>
            </html>
            """

            try:
                send_mail(
                    subject,
                    message,
                    'losvs213@gmail.com',  # Your configured sender email
                    [user.email],  # Send to the user's email
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email to {user.email}: {e}")

# Edit an existing alert
def edit_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST, request.FILES,instance=alert)
        if form.is_valid():
            form.save()
            return redirect('users:admin_dashboard')
    else:
        form = DisasterAlertForm(instance=alert)
    return render(request, 'alerts/edit_alert.html', {'form': form})

# Delete an alert
def delete_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    if request.method == 'POST':
        alert.delete()
        return redirect('users:admin_dashboard')
    return render(request, 'alerts/delete_alert.html', {'alert': alert})

