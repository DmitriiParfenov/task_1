# Create your tests here.
from unittest.mock import patch

from django.core.files import File
from rest_framework import status
from rest_framework.test import APITestCase

from file_manager.models import File as FileModel


class FileListAPITestCase(APITestCase):
    def setUp(self) -> None:
        # Создание объекта File
        self.file = FileModel.objects.create(
            file='../testfile_full.txt'
        )
        self.file.save()


class FileCreateAPITestCase(APITestCase):
    def setUp(self) -> None:
        # Получение маршрутов
        self.create_url = '/file_manager/upload/'

        # Сырые данные для создания объекта модели File
        self.data_full = {'file': File(open('testfile_full.txt', 'rb'))}
        self.data_empty = {'file': File(open('testfile_empty.txt', 'rb'))}

    def test_can_upload_file_with_data(self):
        # Отключение отложенной задачи
        self.patcher = patch('file_manager.tasks.sort_files.delay')
        self.mock_task = self.patcher.start()

        # Количество объектов модели File до POST-запроса
        self.assertFalse(
            FileModel.objects.count()
        )

        # POST-запрос на создание объекта модели File
        response = self.client.post(
            self.create_url,
            self.data_full
        )

        # Проверка статус кода
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Количество объектов модели File после POST-запроса
        self.assertTrue(
            FileModel.objects.count()
        )

        # Включение отложенной задачи
        self.patcher.stop()

    def test_cannot_upload_empty_file(self):
        # Отключение отложенной задачи
        self.patcher = patch('file_manager.tasks.sort_files.delay')
        self.mock_task = self.patcher.start()

        # Количество объектов модели File до POST-запроса
        self.assertFalse(
            FileModel.objects.count()
        )

        # POST-запрос на создание объекта модели File
        response = self.client.post(
            self.create_url,
            self.data_empty
        )

        # Проверка статус кода
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # Количество объектов модели File после POST-запроса
        self.assertFalse(
            FileModel.objects.count()
        )

        # Проверка содержимого ответа
        self.assertEqual(
            response.json(),
            {'file': ['Отправленный файл пуст.']}
        )

        # Включение отложенной задачи
        self.patcher.stop()


class FileListAPIView(FileListAPITestCase):
    def setUp(self) -> None:
        super().setUp()

        # Получение маршрутов
        self.list_url = '/file_manager/files/'

    def test_get_file_objects(self):
        response = self.client.get(
            self.list_url,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'file': 'http://testserver/testfile_full.txt',
                    'processed': False
                },
            ]
        )

        self.assertTrue(
            FileModel.objects.count()
        )

