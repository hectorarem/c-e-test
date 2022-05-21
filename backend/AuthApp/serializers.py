from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        print(validated_data['password'])
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = User
        fields = ("id", "username", "password", "email")

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        exclude = ('user_permissions', 'is_staff', 'is_superuser', 'is_active')

class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions', 'password', 'is_staff', 'is_superuser', 'is_active')

class ReadDetailUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions', 'password', 'is_staff', 'is_superuser', 'is_active')
        depth = 4

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data['user'] = {}
        data['user']['id'] = user.id
        data['user']['username'] = user.username
        data['user']['first_name'] = user.first_name
        data['user']['last_name'] = user.last_name
        data['user']['email'] = user.email
        data['user']['is_active'] = user.is_active
        data['user']['date_joined'] = user.date_joined
        return data