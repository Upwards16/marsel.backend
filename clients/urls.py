from django.urls import path
from .views import (
    ClientListAPIView, ClientCreateAPIView, ClientRetrieveDeleteAPIView, ClientUpdateAPIView,
    TrafficSourceListAPIView, ClientAllListAPIView
)

urlpatterns = [
    path('', ClientListAPIView.as_view(), name="clients"),
    path('all/', ClientAllListAPIView.as_view(), name="clients-all"),
    path('create/', ClientCreateAPIView.as_view(), name="client-create"),
    path('<int:pk>/', ClientRetrieveDeleteAPIView.as_view(), name="client-retrieve-delete"),
    path('update/<int:pk>/', ClientUpdateAPIView.as_view(), name="client-update"),
    path('traffic-sources/', TrafficSourceListAPIView.as_view(), name="client-traffic-sources"),
]
