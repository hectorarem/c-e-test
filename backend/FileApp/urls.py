from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'file', views.FileViewSet, basename='file')

urlpatterns = [
    path('', include(router.urls)),
    path('change/filename/', views.ChangeFileNameApiView.as_view(), name='change-filename')
]
