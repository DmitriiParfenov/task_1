from django.contrib import admin

from file_manager.models import File


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'processed', 'file')
    list_display_links = ('id',)
    search_fields = ('uploaded_at',)
