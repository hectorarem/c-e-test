from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'file', 'uploaded_by', 'file_full_name', 'file_name', 'file_extension', 'file_size']
    list_display_links = ["created_at"]
    list_per_page = 10

    class Meta:
        model = File

admin.site.register(File, FileAdmin)
