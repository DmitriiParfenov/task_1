import datetime

from rest_framework import serializers

from file_manager.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)

    def create(self, validated_data):
        """При создании объекта модели File к текущему названию файла добавляется текущее время и дата."""
        # Получение текущей даты и времени.
        now = datetime.datetime.now().strftime('%d%m%y_%H%M%f')

        # Получение названия файла.
        file_name = validated_data.get('file')

        # Изменение названия файла.
        file_name.name = f'{now}_{file_name}'

        # Создание объекта модели File.
        file_object = File.objects.create(**validated_data)

        return file_object


class FileSerializerList(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'processed')
