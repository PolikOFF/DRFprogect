from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """Модель курса."""
    name = models.CharField(max_length=50, verbose_name='курс')
    preview = models.ImageField(upload_to='online_school/', verbose_name='превью картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец курса', **NULLABLE)

    def __str__(self):
        return f'Курс - {self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Модель урока."""
    course = models.ForeignKey('Course', on_delete=models.CASCADE, **NULLABLE)
    name = models.CharField(max_length=50, verbose_name='урок')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='online_school/', verbose_name='превью картинка', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец урока', **NULLABLE)

    def __str__(self):
        if self.video_url:
            return f'Название курса - {self.name}, ссылка - {self.video_url}'
        return f'Название курса - {self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'уроки'
