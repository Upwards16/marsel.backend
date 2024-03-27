from django.urls import path
from .views import IncomeExpenseChartView, ProjectChartView

urlpatterns = [
    path('cash/charts/', IncomeExpenseChartView.as_view(), name="cash_charts"),
    path('project/charts/', ProjectChartView.as_view(), name="project_charts")
]
