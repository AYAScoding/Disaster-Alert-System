from django.contrib import admin
from .models import DisasterAlert

@admin.register(DisasterAlert)
class DisasterAlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'location' , 'severity', 'date_issued')
    list_filter = ('location', 'type', 'severity')
    search_fields = ('description',)
