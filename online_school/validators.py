from rest_framework import serializers


def video_url_validator(value):
    """Метод для валидации поля ссылки на видео."""
    if 'youtube.com' not in value:
        raise serializers.ValidationError('Введите правильный URL.')
