from django.urls import path
from .views import (
    MarkListAPIView, ColumnListAPIView, TaskListAPIView,
    ParticipantListAPIView, TaskRetrieveDestroyAPIView,
    TaskCreateAPIView, TaskUpdateAPIView, TaskMoveAPIView, TaskUserAllAPIView
)


urlpatterns = [
    path('marks/', MarkListAPIView.as_view(), name="marks"),
    path('columns/', ColumnListAPIView.as_view(), name="columns"),
    path('tasks/', TaskListAPIView.as_view(), name="tasks"),
    path('user/all/', TaskUserAllAPIView.as_view(), name="tasks-all"),
    path('move/', TaskMoveAPIView.as_view(), name="task-move"),
    path('tasks/create/', TaskCreateAPIView.as_view(), name="task-create"),
    path('tasks/<int:pk>/', TaskRetrieveDestroyAPIView.as_view(), name="task_detail"),
    path('tasks/update/<int:pk>/', TaskUpdateAPIView.as_view(), name="task_update"),
    path('participants/', ParticipantListAPIView.as_view(), name="tasks_participants")
]
