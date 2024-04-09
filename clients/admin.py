from django.contrib import admin
from .models import TrafficSource, Client, ClientStatus


@admin.register(TrafficSource)
class TrafficSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientStatus)
class ClientStatus(admin.ModelAdmin):
    pass
