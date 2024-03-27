from .models import Lead, LeadStatus, CallHistory
from rest_framework import serializers
from users.serializers import UserSerializer
from clients.serializers import TrafficSourceSerializer


class LeadStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadStatus
        fields = '__all__'


class CallHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CallHistory
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    status = LeadStatusSerializer(many=False)
    call_history = CallHistorySerializer(many=True)
    traffic_source = TrafficSourceSerializer(many=False)

    class Meta:
        model = Lead
        fields = '__all__'


class LeadCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = '__all__'
