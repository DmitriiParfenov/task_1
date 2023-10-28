import os

from django.core import serializers as core_serializers
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from file_manager.models import File
from file_manager.serializers import FileSerializer, FileSerializerList
from file_manager.tasks import sort_files


# Create your views here.
class FileCreateAPIView(generics.CreateAPIView):
    """Для создания объектов модели File."""

    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        """При создании объекта модели File на уровне представления запускается асинхронная задача для
        обработки файлов."""

        new_file = serializer.save()

        # Получение файла.
        file_obj = serializer.validated_data.get('file')

        # Получение расширения файла.
        file_extension = os.path.splitext(file_obj.name)[1]

        # Сериализация объекта модели File.
        serialized_obj = core_serializers.serialize('json', (new_file,))

        # Запуск асинхронной задачи для обработки файла.
        sort_files.delay(
            file_extension,
            file_obj.name,
            serialized_obj
        )


class FileListAPIView(generics.ListAPIView):
    """Для просмотров объектов модели File."""

    serializer_class = FileSerializerList
    queryset = File.objects.all()
