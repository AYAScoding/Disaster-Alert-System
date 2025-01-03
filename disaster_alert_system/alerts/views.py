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
        form = DisasterAlertForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:admin_dashboard')
    else:
        form = DisasterAlertForm()
    return render(request, 'alerts/add_alert.html', {'form': form})

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

