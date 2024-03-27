from rest_framework import serializers
from .models import Project, Status, WorkStep
from users.serializers import UserListSerializer
from clients.serializers import ClientSerializer


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')


class WorkStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStep
        fields = ('id', 'name', 'done', 'project')


class ProjectSerializer(serializers.ModelSerializer):
    participants = UserListSerializer(read_only=True, many=True)
    work_steps = WorkStepSerializer(many=True, read_only=True)
    status = StatusSerializer(many=False)
    client = ClientSerializer(many=False)

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'start_at', 'end_at', 'cost',
            'additional_info', 'status', 'client', 'terms_of_reference',
            'agreement', 'participants', 'work_steps', 'banner',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context['request'].user.position.slug != 'admin':
            representation['cost'] = None
            representation['agreement'] = None
        return representation

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start_at = validated_data.get('start_at', instance.start_at)
        instance.end_at = validated_data.get('end_at', instance.end_at)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.additional_info = validated_data.get('additional_info', instance.additional_info)
        instance.status = validated_data.get('status', instance.status)
        instance.client = validated_data.get('client', instance.client)
        instance.terms_of_reference = validated_data.get('terms_of_reference', instance.terms_of_reference)
        instance.agreement = validated_data.get('agreement', instance.agreement)
        instance.banner = validated_data.get('banner', instance.banner)

        return instance


class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'start_at', 'end_at', 'cost',
            'additional_info', 'client', 'banner',
            'terms_of_reference', 'agreement', 'status'
        )
