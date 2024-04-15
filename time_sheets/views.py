from rest_framework import generics, filters, status
from config.pagination import CustomPageNumberPagination
from rest_framework.response import Response

from .models import TimeSheet
from .serializers import TimeSheetSerializer, TimeSheetCreateSerializer
from django_filters import rest_framework as dj_filters
from tasks.serializers import TaskSerializer
from projects.serializers import ProjectSerializer
from projects.models import Project
from projects.views import ProjectFilter
from .filters import TimeSheetFilter
from tasks.models import Task


class TimeSheetListCreateAPIView(generics.ListCreateAPIView):
    queryset = TimeSheet.objects.all().order_by('-id')
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.SearchFilter,)
    filterset_class = TimeSheetFilter
    search_fields = ('task__task', )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TimeSheetSerializer
        else:
            return TimeSheetCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user:
            serializer.save(user=user)
        else:
            return Response({"error": "User is not specified"}, status=status.HTTP_400_BAD_REQUEST)

class TimeSheetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSheet.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TimeSheetSerializer
        else:
            return TimeSheetCreateSerializer


class ProjectSearchListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    search_fields = ('name',)

    def get_queryset(self):
        return Project.objects.filter(participants=self.request.user)


class TaskSearchListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project = self.request.GET.get('project', None)
        if project:
            return Task.objects.filter(participants=self.request.user, project=project)
        return Task.objects.filter(participants=self.request.user, project=None)
