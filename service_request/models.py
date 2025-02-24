from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled'),
    ]

    TYPE_CHOICES = [
        ('gas_leak', 'Gas Leak'),
        ('billing_issue', 'Billing Issue'),
        ('new_connection', 'New Connection'),
        ('maintenance', 'Maintenance'),
        ('others','Others'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    request_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.request_type} ({self.status})"