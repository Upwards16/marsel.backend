from django.shortcuts import render
from rest_framework import generics
from .models import Client, TrafficSource, ClientStatus
from .serializers import ClientSerializer, ClientCreateUpdateSerializer, TrafficSourceSerializer, ClientStatus, \
    ClientStatusSerializer
from config.pagination import CustomPageNumberPagination
from django_filters import rest_framework as dj_filters
from django.db import models as dmodels
from .filters import ClientSearchFilter, ClientFilter

class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('-id')
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend, ClientSearchFilter)
    filterset_class = ClientFilter
    search_fields = ('name',)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset


class ClientAllListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('-id')
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = ClientFilter


class ClientRetrieveDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientCreateUpdateSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ClientUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ClientCreateUpdateSerializer
    queryset = Client.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


class TrafficSourceListAPIView(generics.ListAPIView):
    serializer_class = TrafficSourceSerializer
    queryset = TrafficSource.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class ClientStatusListAPIView(generics.ListAPIView):
    serializer_class = ClientStatusSerializer
    queryset = ClientStatus.objects.all()
