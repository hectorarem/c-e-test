import os
from zipfile import ZipFile
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import FileSerializer, ReadFileSerializer
from .models import File

class FileViewSet(ModelViewSet):

    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()
        filter = self.request.GET.get('filter', None)
        if filter:
            queryset = queryset.filter(Q(file__icontains=filter) | Q(uploaded_by__username__icontains=filter)).distinct()
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

class ChangeFileNameApiView(APIView):

    def post(self, request):
        name = self.request.data.get('name', None)
        id = self.request.data.get('id', None)
        ext = self.request.data.get('ext', None)
        if id and name and ext:
            file = File.objects.get(pk=int(id))
            if name != file.file_name:
                clean_file = name.replace(" ", "_").replace("(", '').replace(")", '').replace("[", '').replace("]", '')
                file_name = f'upload/{clean_file}.{ext}.zip'
                if not File.objects.filter(file=file_name).exists():
                    with ZipFile(file.file.path, 'r') as zip_ref:
                        zip_ref.extractall(settings.MEDIA_ROOT / 'upload')
                        old_file_zip = file.file.path
                        old_file = old_file_zip.replace('.zip', '')
                        new_name = f'upload/{name}.{file.file_extension}'
                        new_file = settings.MEDIA_ROOT / new_name
                        os.renames(old_file, new_file)
                        file.file.name = new_name
                        file.save()
                        os.remove(old_file_zip)
                        return JsonResponse({'msg': 'success'})
                else:
                    return JsonResponse(
                        {"msg": "Ya existe un fichero con ese nombre y extension, trate con otro nombre"},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED
                    )
            else:
                return JsonResponse({"msg": "Es el mismo nombre "}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return JsonResponse({"msg": "Faltan datos por enviar"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

