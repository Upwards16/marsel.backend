from django.db import models
from django.contrib.auth import get_user_model
from clients.models import TrafficSource
from clients.serializers import ClientCreateUpdateSerializer
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class LeadStatus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

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

@receiver(post_save, sender=Lead)
def handle_lead_status_change(sender, instance, **kwargs):
    if instance.status.name == 'Завершённый':
        client_data = {
            'name': instance.fullname,
            'phone': instance.phone,
            'email': '',
            'birthday': '',
            'comment': instance.comment,
            'traffic_source': instance.traffic_source,
            'status': 'Не подтвержден',
        }
        client_serializer = ClientCreateUpdateSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            instance.delete()

class CallHistory(models.Model):
    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE,
        related_name="call_history"
    )
    date = models.DateTimeField()
    comment = models.TextField()

    def __str__(self):
        return self.lead.name
