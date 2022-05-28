from django.contrib.auth import get_user_model, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserCreateSerializer, ReadUserSerializer, ReadDetailUserSerializer, UserSerializer, User, \
    CustomTokenObtainPairSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = ReadDetailUserSerializer
    queryset = User.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list': ReadUserSerializer,
            'create': UserCreateSerializer,
            'retrieve': ReadDetailUserSerializer,
            'update': UserSerializer,
            'partial_update': UserSerializer,
            'destroy': UserSerializer
        }


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

