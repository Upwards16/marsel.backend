import operator
from functools import reduce

from django.db import models
from rest_framework import filters
from rest_framework.compat import distinct
from .models import Client, ClientStatus, TrafficSource
from django.contrib.auth import get_user_model
import django_filters

User = get_user_model()


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            'status': ['exact'],
            'manager': ['exact'],
            'traffic_source': ['exact'],
        }

    @property
    def qs(self):
        parent = super().qs
        user = self.request.user

        if user.position and user.position.name == 'admin':
            return parent

        elif user.position and user.position.name == 'Менеджер по продажам':
            return parent.filter(manager=user)

        else:
            return parent.none()





