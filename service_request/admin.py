from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'request_type')
    search_fields = ('name', 'email', 'phone')
