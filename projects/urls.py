from django.urls import path
from .views import (
    ProjectListAPIView, WorkStepCreateAPIView, WorkStepRetrieveUpdateDestroyAPIView,
    ParticipantsCreateAPIView, ParticipantsDeleteAPIView, ProjectRetrieveDestroyAPIViewAPIView,
    StatusListAPIView, ParticipantSearchAPIView,
    ProjectCreateAPIView, ProjectUpdateAPIView
)

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name="projects"),
    path('create/', ProjectCreateAPIView.as_view(), name="project_create"),
    path('update/<int:pk>/', ProjectUpdateAPIView.as_view(), name="project_update"),
    path('statuses/', StatusListAPIView.as_view(), name="work-step-create"),
    path('work-steps/', WorkStepCreateAPIView.as_view(), name="work-step-create"),
    path('work-steps/<int:pk>/', WorkStepRetrieveUpdateDestroyAPIView.as_view(), name="work-step"),
    path('participants/', ParticipantsCreateAPIView.as_view(), name="participants-create"),
    path('participants/delete/', ParticipantsDeleteAPIView.as_view(), name="participants-delete"),
    path('<int:pk>/', ProjectRetrieveDestroyAPIViewAPIView.as_view(), name="project-detail"),
    path('participants/search/', ParticipantSearchAPIView.as_view(), name="participant_search")
]
