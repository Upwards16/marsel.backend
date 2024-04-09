from .serializers import (
    PaymentTypeSerializer, IncomeSerializer,
    IncomeCreateSerializer, ExpenseTypeSerializer,
    ExpenseSerializer, ExpenseCreateSerializer
)
from .filters import ExpenseFilter, IncomeFilter
from rest_framework import generics, filters
from .models import PaymentType, Income, Expense, ExpenseType
from config.pagination import CustomPageNumberPagination
from django_filters import rest_framework as dj_filters


class PaymentTypeListAPIView(generics.ListCreateAPIView):

    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class IncomeListCreateAPIView(generics.ListCreateAPIView):

    pagination_class = CustomPageNumberPagination
    queryset = Income.objects.all().order_by('-id')
    filter_backends = (dj_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = IncomeFilter
    search_fields = ("account_number",)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return IncomeCreateSerializer
        return IncomeSerializer


class IncomeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = IncomeCreateSerializer
    queryset = Income.objects.all()


class ExpenseTypeListAPIView(generics.ListCreateAPIView):

    serializer_class = ExpenseTypeSerializer
    queryset = ExpenseType.objects.all()


class ExpenseListCreateAPIView(generics.ListCreateAPIView):

    pagination_class = CustomPageNumberPagination
    queryset = Expense.objects.all()
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ExpenseCreateSerializer
        return ExpenseSerializer


class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseCreateSerializer
    queryset = Expense.objects.all()
