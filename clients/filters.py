import operator
from functools import reduce

from django.db import models
from rest_framework import filters
from rest_framework.compat import distinct
from .models import Client

import django_filters as dj_filters

class ClientFilter(dj_filters.FilterSet):
    manager = dj_filters.CharFilter(field_name='manager__fullname', lookup_expr='icontains')
    status = dj_filters.CharFilter(field_name='status__name', lookup_expr='icontains')
    traffic_source = dj_filters.CharFilter(field_name='traffic_source__name', lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['manager', 'status', 'traffic_source']

class ClientSearchFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if len(search_terms) == 0:
            return Client.objects.all()

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]

        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))

        queryset = queryset.filter(reduce(operator.and_, conditions))

        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset)

        return self.filter_by_user_position(request.user, queryset)

    def filter_by_user_position(self, user, queryset):
        if user.position and user.position.name == 'admin':
            return queryset
        elif user.position and user.position.name == 'Менеджер по продажам':
            return queryset.filter(manager=user, status__name='Подтвержден')
        else:
            return queryset.none()



