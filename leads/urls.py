from django.urls import path
from .views import (
    LeadStatusListAPIView, LeadListCreateAPIView,
    CallHistoryCreateAPIView, LeadRetrieveUpdateDestroyAPIView,
    CallHistoryRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('statuses/', LeadStatusListAPIView.as_view(), name="lead_statuses"),
    path('', LeadListCreateAPIView.as_view(), name="leads"),
    path('<int:pk>/', LeadRetrieveUpdateDestroyAPIView.as_view(), name="lead_detail"),
    path('call-history/', CallHistoryCreateAPIView.as_view(), name="leads_call_history"),
    path(
        'call-history/<int:pk>/',
        CallHistoryRetrieveUpdateDestroyAPIView.as_view(),
        name="call_history_detail"
    )
]
