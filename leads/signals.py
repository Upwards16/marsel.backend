from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from clients.serializers import ClientCreateUpdateSerializer
from django.db import transaction


@receiver(post_save, sender=Lead)
def handle_lead_status_change(sender, instance, **kwargs):
    if instance.status.is_finished:
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
                instance.delete()
        else:
            pass
