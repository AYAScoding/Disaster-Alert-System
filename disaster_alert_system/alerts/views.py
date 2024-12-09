from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import DisasterAlertForm
from .models import DisasterAlert

# Admin-only decorator
def admin_required(user):
    return user.is_staff  # or user.is_superuser, depending on your logic

@user_passes_test(admin_required)
def create_alert(request):
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user  # Assign the logged-in admin
            alert.save()
            return redirect('alerts:homeAlerts')  # Redirect to alerts home page
    else:
        form = DisasterAlertForm()
    return render(request, 'alerts/create_alert.html', {'form': form})


def homeAlert(request):
    alerts = []
    if request.user.is_authenticated:
        user_location = request.user.profile.location  # Fetch user's location from their profile
        if user_location:
            alerts = DisasterAlert.objects.filter(location=user_location).order_by('-date_issued')
    return render(request, 'alerts/homeAlert.html', {'alerts': alerts})













'''from django.shortcuts import render, get_object_or_404, redirect
from .models import DisasterAlert
from .forms import DisasterAlertForm
from django.contrib.auth.decorators import login_required
from .notifications import send_alert_notification

@login_required
def dashboard(request):
    alerts = DisasterAlert.objects.filter(user=request.user)
    if not alerts:
        alerts_message = "No alerts to display at the moment."
    else:
        alerts_message = None
    return render(request, 'dashboard.html', {'alerts': alerts, 'alerts_message': alerts_message})

@login_required
def create_alert(request):
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            send_alert_notification(alert)
            return redirect('alerts:alert_list')
    else:
        form = DisasterAlertForm()
    
    return render(request, 'alerts/create_alert.html', {'form': form})

def alert_list(request):
    alerts = DisasterAlert.objects.all()
    return render(request, 'alerts/alert_list.html', {'alerts': alerts})

def alert_detail(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    return render(request, 'alerts/alert_detail.html', {'alert': alert})

@login_required
def update_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.save()
            return redirect('alerts:alert_list')
    else:
        form = DisasterAlertForm(instance=alert)
    
    return render(request, 'alerts/update_alert.html', {'form': form, 'alert': alert})

@login_required
def delete_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    alert.delete()
    return redirect('alerts:alert_list')'''
