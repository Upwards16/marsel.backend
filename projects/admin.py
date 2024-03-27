from django.contrib import admin
from .models import Project, Status


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
