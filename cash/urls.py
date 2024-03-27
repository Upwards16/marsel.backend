from django.urls import path
from .views import (
    PaymentTypeListAPIView, IncomeListCreateAPIView,
    ExpenseListCreateAPIView, ExpenseTypeListAPIView,
    IncomeRetrieveUpdateDestroyAPIView,
    ExpenseRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('payment-types/', PaymentTypeListAPIView.as_view(), name="payment_type_list"),
    path('incomes/', IncomeListCreateAPIView.as_view(), name="cash_incomes"),
    path('incomes/<int:pk>/', IncomeRetrieveUpdateDestroyAPIView.as_view(), name="income_detail"),
    path('expense-types/', ExpenseTypeListAPIView.as_view(), name="expense_type_list"),
    path('expenses/', ExpenseListCreateAPIView.as_view(), name="cash_expenses"),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyAPIView.as_view(), name="expense_detail"),
]
