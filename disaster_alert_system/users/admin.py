from django.contrib import admin
from .models import Profile



admin.site.site_header = "Disaster Alert System Administration"
admin.site.site_title = "Disaster Alert Admin Portal"
admin.site.index_title = "Welcome to the Disaster Alert Admin Dashboard"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Display user attributes (username, email) and profile attributes (phone, location)
    list_display = ['user', 'get_username', 'get_email', 'location']
    
    # Filter by location
    list_filter = ['location']
    
    # Enable search on user attributes (username, email), and profile attributes (phone, location)
    search_fields = ['user__username', 'user__email', 'location']







    
    
    # Custom methods to display the username and email of the associated user
    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user__username'  # Allow sorting by username
    get_username.short_description = 'Username'  # Set display name for the column

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'  # Allow sorting by email
    get_email.short_description = 'Email'  # Set display name for the column
