from config.pagination import CustomPageNumberPagination
from django.contrib.auth import get_user_model
from django_filters import rest_framework as dj_filters
from rest_framework import generics, views, status
from rest_framework.response import Response
from users.serializers import UserSerializer

from .filters import ProjectSearchFilter, ParticipantSearchFilter
from .models import Project, WorkStep, Status
from .serializers import (
    ProjectSerializer, WorkStepSerializer, StatusSerializer, ProjectCreateSerializer
)

User = get_user_model()


class ProjectFilter(dj_filters.FilterSet):

    class Meta:
        model = Project
        fields = ('client', 'status')


class StatusListAPIView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('-id')
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend, ProjectSearchFilter)
    filterset_class = ProjectFilter
    search_fields = ('name',)
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    queryset = Project.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class ProjectRetrieveDestroyAPIViewAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class ProjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectCreateSerializer
    queryset = Project.objects.all()


class WorkStepCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkStepSerializer
    queryset = WorkStep.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class WorkStepRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkStepSerializer
    queryset = WorkStep.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


class ParticipantsCreateAPIView(views.APIView):
    def post(self, request):
        participants = request.data.get('participants', [])
        project = request.data.get('project', None)
        if project is not None:
            project = Project.objects.filter(id=project).first()

            if project is not None:
                users = User.objects.filter(id__in=participants)
                project.participants.add(*users)
                response_data = {"message": "Success", "status": 200}
                status_code = status.HTTP_200_OK
            else:
                response_data = {"message": "Project not found"}
                status_code = status.HTTP_404_NOT_FOUND
        else:
            response_data = {"error": "Project is required"}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=status_code)


class ParticipantsDeleteAPIView(views.APIView):

    def post(self, request):
        participant = request.data.get('participant')
        project = request.data.get('project', None)
        if project is not None:
            project = Project.objects.filter(id=project).first()

            if project is not None:
                users = User.objects.filter(id=participant)
                project.participants.remove(*users)
                response_data = {"message": "Success", "status": 204}
                status_code = status.HTTP_204_NO_CONTENT
            else:
                response_data = {"message": "Project not found"}
                status_code = status.HTTP_404_NOT_FOUND
        else:
            response_data = {"error": "Project is required"}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=status_code)


class ParticipantSearchAPIView(generics.ListAPIView):

    serializer_class = UserSerializer
    filter_backends = (ParticipantSearchFilter,)
    search_fields = ('firstname', 'lastname',)
    queryset = User.objects.all()
