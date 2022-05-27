from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file', 'uploaded_by']

    def create(self, validated_data):
        file = validated_data['file']
        clean_file = file.name.replace(" ", "_").replace("(", '').replace(")", '').replace("[", '').replace("]", '')
        file_name = f'upload/{clean_file}.zip'
        print(file_name)
        if File.objects.filter(file=file_name).exists():
            raise serializers.ValidationError({
                'msg': 'Ya tenemos un fichero con ese nombre, por favor, cambie el nombre e intente nuevamente'
            })
        return super().create(validated_data)

class ReadFileSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id', 'created_at', 'updated_at', 'file', 'uploaded_by', 'file_full_name',
                  'file_name', 'file_extension', 'file_size']

    def get_uploaded_by(self, obj):
        return obj.uploaded_by.username