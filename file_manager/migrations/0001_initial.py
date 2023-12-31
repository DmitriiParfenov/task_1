# Generated by Django 4.2.6 on 2023-10-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата загрузки')),
                ('processed', models.BooleanField(default=False, verbose_name='Обработка файла')),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ('-uploaded_at',),
            },
        ),
    ]
