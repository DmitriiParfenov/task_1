from django.urls import path

from file_manager.apps import FileManagerConfig
from file_manager.views import FileCreateAPIView, FileListAPIView

app_name = FileManagerConfig.name

urlpatterns = [
    path('upload/', FileCreateAPIView.as_view(), name='file_create'),
    path('files/', FileListAPIView.as_view(), name='file-list'),
]
