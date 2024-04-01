from django.contrib import admin
from .models import TimeSheet
# Register your models here.


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'date', 'time', 'comment')
    list_filter = ('user', 'task__project', 'date')
    search_fields = ('task__task', 'comment')
    date_hierarchy = 'date'