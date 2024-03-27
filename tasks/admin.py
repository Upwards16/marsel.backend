from django.contrib import admin
from .models import Mark, Column, Task


@admin.register(Mark)
class MarkModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    pass
