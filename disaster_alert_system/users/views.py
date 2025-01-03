from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LoginForm
from alerts.models import DisasterAlert
from django.shortcuts import get_object_or_404


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # The save method in the form now handles everything
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Password1 is used for UserCreationForm
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Log in the user and set session data
                login(request, user)
                request.session['user_id'] = user.id  # Store user ID in the session

            return redirect('users:home')
        else:
            # Add messages for specific errors if needed
            if 'username' in form.errors:
                messages.error(request, 'Username already exists.')
            if 'password2' in form.errors:
                messages.error(request, 'Passwords do not match.')
            # You can add more custom error handling for other fields as needed
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # This automatically manages the session
                # Store only the user ID in the session
                request.session['user_id'] = user.id
                return redirect('users:home')
            else:
               messages.error(request, 'Invalid username or password')
        else:
            messages.error(request,'Invalid username or password')            
            form = LoginForm()           
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def landing_page(request):
    return render(request, 'landing.html')


def edit_profile(request):
    if request.method == "POST":
       
        password = request.POST.get("password")
        location = request.POST.get("location")

        user = request.user
       

        if password:
            user.set_password(password)

       
        if hasattr(user, "profile") and location:
            user.profile.location = location
            user.profile.save()

        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("users:edit_profile")

    return render(request, "users/edit_profile.html")

def logout_view(request):
    logout(request)
    return redirect('users:landing')

# session 
def profile_view(request):
    user_id = request.session.get('user_id')  # Retrieve the user ID from the session
    if user_id:
        user = User.objects.get(id=user_id)  # Query the database for the user
        return render(request, 'home.html', {'user': user})
    else:
        return redirect('login')  # Redirect if no session exists
    

def password_reset(request):
    return render(request, 'password_reset.html')

def admin_dashboard(request):
    total_users = User.objects.count()
    total_alerts = DisasterAlert.objects.count()
    active_alerts = DisasterAlert.objects.filter(severity='High').count()
    users = User.objects.all()
    alerts = DisasterAlert.objects.all()

    context = {
        'total_users': total_users,
        'total_alerts': total_alerts,
        'active_alerts': active_alerts,
        'users': users,
        'alerts': alerts,
    }
    return render(request, 'users/admin_dashboard.html', context)


def admin_check(user):
    return user.is_staff or user.is_superuser


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        
        return redirect("users:admin_dashboard")

    return render(request, "users/delete_user.html", {"user": user})


def add_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_staff = request.POST.get("is_staff") == "on"

        if username and email and password:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.is_staff = is_staff
            new_user.save()
           
        else:
            messages.error(request, "Please fill in all fields.")

        return redirect("users:admin_dashboard")
    
    return render(request, "users/add_user.html")


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.username = request.POST.get("username", user.username)
        user.email = request.POST.get("email", user.email)
        password = request.POST.get("password")

        if password:
            user.set_password(password)

        user.is_staff = request.POST.get("is_staff") == "on"
        user.save()

        
        return redirect("users:admin_dashboard")

    return render(request, "users/edit_user.html", {"user": user})



def contacts(request):
    # Sample contact data
    contact_list = [
        
    {"name": "Fire Department", "phone": "199", "email": "firedept@northcyprus.gov"},
    {"name": "Police Department", "phone": "155", "email": "police@northcyprus.gov"},
    {"name": "Medical Emergency", "phone": "112", "email": "ambulance@northcyprus.gov"}


    ]
    return render(request, 'users/contacts.html', {'contacts': contact_list})


