from django.db import models


# Create your models here.
class File(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата загрузки')
    processed = models.BooleanField(default=False, verbose_name='Обработка файла')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f'Файл загружен {self.uploaded_at}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ('-uploaded_at',)
