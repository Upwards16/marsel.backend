from rest_framework import serializers
from .models import Client, TrafficSource, ClientStatus
from users.serializers import UserListSerializer

class ClientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientStatus
        fields = ('id', 'name', 'slug')

class TrafficSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficSource
        fields = ('id', 'name')


class ClientSerializer(serializers.ModelSerializer):
    traffic_source = TrafficSourceSerializer(many=False)
    status = ClientStatusSerializer(many=False)
    manager = UserListSerializer(many=False)

    class Meta:
        model = Client
        fields = (
            'id', 'name', 'phone', 'email', 'birthday', 'comment', 'manager', 'traffic_source', 'status'
        )


class ClientCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'id', 'name', 'phone', 'email', 'birthday', 'comment', 'manager', 'traffic_source', 'status'
        )

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.traffic_source = validated_data.get('traffic_source', instance.traffic_source)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
