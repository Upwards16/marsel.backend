from rest_framework import serializers
from .models import Mark, Column, Task
from projects.serializers import ProjectSerializer
from users.serializers import UserSerializer
from users.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    column = ColumnSerializer(many=False)
    project = ProjectSerializer(many=False)
    mark = MarkSerializer(many=False)
    participants = UserSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
