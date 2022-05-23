from rest_framework.viewsets import ModelViewSet
from .serializers import FileSerializer, ReadFileSerializer
from .models import File

class FileViewSet(ModelViewSet):

    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list': ReadFileSerializer,
            'create': FileSerializer,
            'retrieve': ReadFileSerializer,
            'update': FileSerializer,
            'partial_update': FileSerializer,
            'destroy': FileSerializer
        }

    def get_serializer_class(self, *args, **kwargs):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
