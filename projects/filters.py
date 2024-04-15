import operator
from functools import reduce

from django.db import models
from rest_framework import filters
from rest_framework.compat import distinct
from django.contrib.auth import get_user_model
import django_filters
from .models import Project

User = get_user_model()


class ProjectSearchFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)
        if len(search_terms) == 0:
            return Project.objects.all()

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
        return queryset


class ParticipantSearchFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        project_id = request.query_params.get('project')
        if project_id:
            project = Project.objects.filter(id=project_id).first()
        search_terms = self.get_search_terms(request)
        if len(search_terms) == 0:
            return User.objects.none()

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
        if project is not None:
            return queryset.exclude(pk__in=project.participants.all().values_list('pk', flat=True))
        return queryset

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'status': ['exact'],
            'client': ['exact'],
        }
