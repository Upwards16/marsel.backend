import operator
from functools import reduce

from django.db import models
from rest_framework import filters
from rest_framework.compat import distinct
from .models import Client


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

        base = queryset
        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.and_, conditions))

        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset, base)

        user = request.user
        if user.position and user.position.name == 'admin':
            return queryset
        elif user.position and user.position.name == 'Менеджер по продажам':
            return queryset.filter(manager=user)
        else:
            return queryset.none()
