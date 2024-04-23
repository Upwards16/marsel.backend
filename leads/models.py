from django.db import models
from django.contrib.auth import get_user_model
from clients.models import TrafficSource
from datetime import datetime
User = get_user_model()


class LeadStatus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Lead(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name="leads",
        null=True
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    reminder_date = models.DateTimeField()
    traffic_source = models.ForeignKey(
        TrafficSource, on_delete=models.SET_NULL,
        related_name="leads",
        null=True
    )
    comment = models.TextField(null=True)
    status = models.ForeignKey(
        LeadStatus, on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.full_name

class CallHistory(models.Model):
    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE,
        related_name="call_history"
    )
    date = models.DateTimeField(blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.lead.full_name

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.now()
        super().save(*args, **kwargs)