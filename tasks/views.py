from rest_framework import generics, response, views, status, permissions
from rest_framework.response import Response
from django.db import connection
from .models import Column, Mark, Task
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from .filters import TaskSearchFilter
from .serializers import (
    MarkSerializer, ColumnSerializer,
    TaskSerializer, TaskCreateSerializer,
)
from config.pagination import CustomPageNumberPagination
from django_filters import rest_framework as dj_filters

User = get_user_model()


class MarkListAPIView(generics.ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class ColumnListAPIView(generics.ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend, TaskSearchFilter)
    filterset_fields = ('column', 'project', 'mark',)
    serializer_class = TaskSerializer

class TaskUserAllAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [TaskSearchFilter]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            queryset = Task.objects.filter(participants=user)
            return queryset
        else:
            return Task.objects.none()

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskMoveAPIView(views.APIView):

    def post(self, request):
        destination = request.data.get('destination')
        source = request.data.get('source')
        new_position = int(destination['index']) + 1
        old_position = int(source['index']) + 1
        column_change = True if destination['droppableId'] != source['droppableId'] else False
        task_id = int(request.data.get('draggableId'))

        with connection.cursor() as cursor:
            cursor.execute(
                f'UPDATE tasks_task '
                f'SET position={new_position}, column_id={destination["droppableId"]} '
                f'WHERE id = {task_id}')

            if new_position > 1:
                if column_change:
                    print(column_change)
                    cursor.execute(
                        f'UPDATE tasks_task SET position=position+1 WHERE position >= {new_position} and id != {task_id}')
                else:
                    if new_position > old_position:
                        cursor.execute(
                            f'UPDATE tasks_task SET position=position-1 WHERE position > {old_position} and position <= {new_position} and id != {task_id}')
                    else:
                        cursor.execute(
                            f'UPDATE tasks_task SET position=position+1 WHERE position < {old_position} and position >= {new_position} and id != {task_id}')

            else:
                cursor.execute(
                    f'UPDATE tasks_task SET position=position+1 WHERE position >= {new_position} and id != {task_id}')

        return Response({
            "list_of_expense_amount": [],
        }, status=status.HTTP_200_OK)

class ParticipantListAPIView(generics.ListAPIView):

    serializer_class = UserSerializer
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_fields = ('project',)
    queryset = User.objects.all()
