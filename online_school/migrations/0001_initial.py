# Generated by Django 5.0.4 on 2024-04-09 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='курс')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='online_school/', verbose_name='превью картинка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='урок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='online_school/', verbose_name='превью картинка')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_school.course')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]