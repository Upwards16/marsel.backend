from django.contrib import admin
from .models import TrafficSource, Client


@admin.register(TrafficSource)
class TrafficSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
