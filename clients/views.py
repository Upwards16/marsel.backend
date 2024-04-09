from django.shortcuts import render
from rest_framework import generics
from .models import Client, TrafficSource
from .serializers import ClientSerializer, ClientCreateUpdateSerializer, TrafficSourceSerializer
from config.pagination import CustomPageNumberPagination
from django_filters import rest_framework as dj_filters
from django.db import models as dmodels


class ClientFilter(dj_filters.FilterSet):

    class Meta:
        model = Client
        fields = ('traffic_source', 'status')


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = ClientFilter


class ClientAllListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
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
