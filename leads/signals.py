from django.db.models.signals import post_save
from django.dispatch import receiver
from leads.models import Lead
from clients.serializers import ClientCreateUpdateSerializer
from django.dispatch import receiver

@receiver(post_save, sender=Lead)
def handle_lead_status_change(sender, instance, **kwargs):
    if instance.status.name.strip() == 'Завершённый':
        client_data = {
            'name': instance.full_name,
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