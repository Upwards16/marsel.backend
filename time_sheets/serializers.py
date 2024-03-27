from rest_framework import serializers
from .models import TimeSheet
from users.serializers import UserSerializer
from tasks.serializers import TaskSerializer


class TimeSheetSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    task = TaskSerializer(many=False)

    class Meta:
        model = TimeSheet
        fields = '__all__'


class TimeSheetCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSheet
        fields = '__all__'
