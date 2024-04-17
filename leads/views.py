from config.pagination import CustomPageNumberPagination
from django_filters import rest_framework as dj_filters
from rest_framework import generics

from .filters import LeadFilter
from .models import Lead, LeadStatus, CallHistory
from .serializers import (
    LeadStatusSerializer,
    LeadSerializer,
    LeadCreateSerializer,
    CallHistorySerializer
)


class LeadStatusListAPIView(generics.ListAPIView):
    queryset = LeadStatus.objects.all()
    serializer_class = LeadStatusSerializer


class LeadListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all().order_by('status__is_finished', '-id')
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = LeadFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeadCreateSerializer
        return LeadSerializer


class LeadRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Lead.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LeadSerializer
        else:
            return LeadCreateSerializer


class CallHistoryCreateAPIView(generics.CreateAPIView):

    queryset = CallHistory.objects.all()
    serializer_class = CallHistorySerializer


class CallHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CallHistory.objects.all()
    serializer_class = CallHistorySerializer


