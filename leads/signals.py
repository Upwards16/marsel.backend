from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from clients.serializers import ClientCreateUpdateSerializer
from django.db import transaction
from datetime import timedelta
from .tasks import send_reminder_notification_to_email, send_reminder_notification_to_telegram

@receiver(post_save, sender=Lead)
def handle_lead_status_change(sender, instance, **kwargs):
    if instance.status.is_finished:
        if instance.user is not None:
            client_data = {
                'name': instance.full_name,
                'phone': instance.phone,
                'email': '',
                'birthday': None,
                'comment': instance.comment,
                'status': 2,
                'manager': instance.user.pk,
                'traffic_source': instance.traffic_source.pk,
            }
            client_serializer = ClientCreateUpdateSerializer(data=client_data)
            if client_serializer.is_valid():
                with transaction.atomic():
                    client = client_serializer.save()
            else:
                pass

@receiver(post_save, sender=Lead)
def schedule_reminder_notification_to_email(sender, instance, created, **kwargs):
    if created:
        reminder_time = instance.reminder_date
        notification_time = reminder_time - timedelta(hours=3)
        send_reminder_notification_to_email.apply_async((instance.id,), eta=notification_time)

@receiver(post_save, sender=Lead)
def schedule_reminder_notification_to_telegram(sender, instance, created, **kwargs):
    if created:
        reminder_time = instance.reminder_date
        notification_time = reminder_time - timedelta(hours=3)
        send_reminder_notification_to_telegram.apply_async((instance.id,), eta=notification_time)
