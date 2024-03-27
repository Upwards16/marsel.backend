from config.pagination import CustomPageNumberPagination
from django_filters import rest_framework as dj_filters
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Position, Status
from .serializers import (
    UserSerializer, PositionSerializer, UserCreateSerializer, UserListSerializer, UserUpdateSerializer,
    StatusSerializer, CustomTokenObtainPairSerializer
)


class UserFilter(dj_filters.FilterSet):
    class Meta:
        model = User
        fields = ('status', 'position__slug', 'position',)


class UserInfoView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class PositionAPIView(generics.ListAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class StatusAPIView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class UserAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.filter(is_superuser=False)
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = UserFilter


class UserRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    # permission_classes = (permissions.IsAuthenticated,)
