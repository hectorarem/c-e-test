from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]