import os
import shutil

from celery import shared_task
from django.core import serializers as core_serializers

from file_manager.models import File


@shared_task
def sort_files(extension, file_name, file_object):
    """Метод сортирует файлы по расширениям в соответствующие папки. После сортировки изменяется значение поля
    <processed> модели File на True."""

    # Исполняемые файлы
    if extension.lower() in ('.exe', '.com', '.bat'):
        if not os.path.isdir('media/files/Frozen_binaries'):
            os.mkdir('media/files/Frozen_binaries')
        shutil.move(f'media/files/{file_name.name.replace(" ", "_")}',
                    f'media/files/Frozen_binaries/{file_name.name.replace(" ", "_")}')
        for obj in core_serializers.deserialize('json', file_object):
            obj_id = obj.object.id
            file_obj = File.objects.get(pk=obj_id)
            file_obj.processed = True
            file_obj.save()

    # Файлы Microsoft office
    elif extension.lower() in ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'):
        if not os.path.isdir('media/files/Microsoft_office'):
            os.mkdir('media/files/Microsoft_office')
        shutil.move(f'media/files/{file_name.replace(" ", "_")}',
                    f'media/files/Microsoft_office/{file_name.replace(" ", "_")}')
        for obj in core_serializers.deserialize('json', file_object):
            obj_id = obj.object.id
            file_obj = File.objects.get(pk=obj_id)
            file_obj.processed = True
            file_obj.save()

    # Изображения
    elif extension.lower() in ('.png', '.jpg', '.jpeg'):
        if not os.path.isdir('media/files/Pictures'):
            os.mkdir('media/files/Pictures')
        shutil.move(f'media/files/{file_name.name.replace(" ", "_")}',
                    f'media/files/Pictures/{file_name.name.replace(" ", "_")}')
        for obj in core_serializers.deserialize('json', file_object):
            obj_id = obj.object.id
            file_obj = File.objects.get(pk=obj_id)
            file_obj.processed = True
            file_obj.save()

    # Видео
    elif extension.lower() in ('.mvc', '.flv', '.mov', '.3gp', '.avi', '.mp4', '.mpg', '.mkv'):
        if not os.path.isdir('media/files/Video'):
            os.mkdir('media/files/Video')
        shutil.move(f'media/files/{file_name.name.replace(" ", "_")}',
                    f'media/files/Video/{file_name.name.replace(" ", "_")}')
        for obj in core_serializers.deserialize('json', file_object):
            obj_id = obj.object.id
            file_obj = File.objects.get(pk=obj_id)
            file_obj.processed = True
            file_obj.save()

    # Архивы
    elif extension.lower() in ('.zip', '.rar'):
        if not os.path.isdir('media/files/Archives'):
            os.mkdir('media/files/Archives')
        shutil.move(f'media/files/{file_name.name.replace(" ", "_")}',
                    f'media/files/Archives/{file_name.name.replace(" ", "_")}')
        for obj in core_serializers.deserialize('json', file_object):
            obj_id = obj.object.id
            file_obj = File.objects.get(pk=obj_id)
            file_obj.processed = True
            file_obj.save()

    # Все остальные файлы
    else:
        if not os.path.isdir('media/files/others'):
            os.mkdir('media/files/others')
        shutil.move(f'media/files/{file_name.name.replace(" ", "_")}',
                    f'media/files/others/{file_name.name.replace(" ", "_")}')
        for obj in core_serializers.deserialize('json', file_object):
            obj_id = obj.object.id
            file_obj = File.objects.get(pk=obj_id)
            file_obj.processed = True
            file_obj.save()
