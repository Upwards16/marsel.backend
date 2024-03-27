from .models import PaymentType, Income, Expense, ExpenseType
from rest_framework import serializers
from projects.serializers import ProjectCreateSerializer


class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'


class IncomeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    project = ProjectCreateSerializer(many=False)
    payment_type = PaymentTypeSerializer(many=False)

    class Meta:
        model = Income
        fields = '__all__'


class ExpenseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseType
        fields = '__all__'


class ExpenseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    expense_type = ExpenseTypeSerializer(many=False)

    class Meta:
        model = Expense
        fields = '__all__'
