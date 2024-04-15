from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import filters
from .models import Task
User = get_user_model()

class TaskSearchFilter(filters.SearchFilter):
    search_param = 'search'

    def filter_queryset(self, request, queryset, view):
        search_value = request.query_params.get(self.search_param)

        if search_value:
            queryset = queryset.filter(
                Q(task__icontains=search_value) |
                Q(project__name__icontains=search_value)
            ).distinct()

        return queryset
