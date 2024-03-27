from django.urls import path
from .views import (
    TimeSheetListCreateAPIView, TimeSheetRetrieveUpdateDestroyAPIView, ProjectSearchListAPIView,
    TaskSearchListAPIView
)

urlpatterns = [
    path('sheets/', TimeSheetListCreateAPIView.as_view(), name="sheets"),
    path('sheets/projects/', ProjectSearchListAPIView.as_view(), name="sheets-project-list"),
    path('sheets/tasks/', TaskSearchListAPIView.as_view(), name="sheets-task-list"),
    path('sheets/<int:pk>/', TimeSheetRetrieveUpdateDestroyAPIView.as_view(), name="sheet_detail")
]

