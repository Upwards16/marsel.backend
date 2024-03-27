from django_filters import rest_framework as dj_filters
from .models import Expense, Income


class ExpenseFilter(dj_filters.FilterSet):
    start_date = dj_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = dj_filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Expense
        fields = (
            'start_date',
            'end_date',
            'expense_type'
        )


class IncomeFilter(dj_filters.FilterSet):
    start_date = dj_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = dj_filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Income
        fields = (
            'start_date',
            'end_date',
        )
