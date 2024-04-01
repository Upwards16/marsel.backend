from rest_framework import serializers
from .models import TimeSheet
from users.serializers import UserSerializer
from tasks.serializers import TaskSerializer


class TimeSheetSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    task = TaskSerializer(many=False)
    date = serializers.SerializerMethodField()

    class Meta:
        model = TimeSheet
        fields = '__all__'
    def get_date(self, obj):
        date_value = obj.date

        formatted_date = date_value.strftime('%d-%m-%Y')

        return formatted_date

class TimeSheetCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSheet
        fields = '__all__'
