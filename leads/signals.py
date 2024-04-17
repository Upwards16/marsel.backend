from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from clients.serializers import ClientCreateUpdateSerializer
from django.db import transaction
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail

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


# @shared_task
# def send_reminder_email(lead_id):
#     lead = Lead.objects.get(pk=lead_id)
#     subject = 'Напоминание: {} ожидает вашего контакта'.format(lead.full_name)
#     message = 'Пожалуйста, не забудьте связаться с {} по телефону {}.'.format(lead.full_name, lead.phone)
#     send_mail(subject, message, 'from@example.com', [lead.user.email])
#
# @receiver(post_save, sender=Lead)
# def schedule_reminder_email(sender, instance, created, **kwargs):
#     if created:
#         reminder_time = instance.reminder_date - timezone.timedelta(minutes=3)
#         send_reminder_email.apply_async(args=[instance.pk], eta=reminder_time)
