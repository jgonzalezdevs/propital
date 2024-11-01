from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ("ALERT", "Alert"),
        ("WARNING", "Warning"),
        ("INFO", "Info"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=7,choices=NOTIFICATION_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    is_read = models.BooleanField(default=False)
