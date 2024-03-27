from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    UserAPIView, UserRetrieveDestroyAPIView, PositionAPIView, UserCreateAPIView, UserUpdateAPIView,
    StatusAPIView, CustomTokenObtainPairView, UserInfoView
)

urlpatterns = [
    path('users/', UserAPIView.as_view(), name="users"),
    path('me/', UserInfoView.as_view(), name="user-info"),
    path('users/create/', UserCreateAPIView.as_view(), name="user-create"),
    path('users/<int:pk>/', UserRetrieveDestroyAPIView.as_view(), name="user-detail"),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name="user-update"),
    path('user/positions/', PositionAPIView.as_view(), name="positions"),
    path('user/statuses/', StatusAPIView.as_view(), name="statuses"),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
