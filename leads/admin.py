from django.contrib import admin
from .models import Lead, LeadStatus, CallHistory

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(LeadStatus)
class LeadStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(CallHistory)
class CallHistoryAdmin(admin.ModelAdmin):
    pass
