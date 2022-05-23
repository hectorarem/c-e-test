from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file', 'uploaded_by']

class ReadFileSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id', 'created_at', 'updated_at', 'file', 'uploaded_by', 'file_full_name',
                  'file_name', 'file_extension', 'file_size']

    def get_uploaded_by(self, obj):
        return obj.uploaded_by.username