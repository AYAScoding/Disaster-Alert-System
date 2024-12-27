from django.contrib import admin
from .models import DisasterAlert

@admin.register(DisasterAlert)
class DisasterAlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'location' , 'severity', 'date_issued','image')
    list_filter = ('location', 'type','id', 'severity')
    search_fields = ('description',)
