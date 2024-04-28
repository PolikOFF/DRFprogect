from rest_framework.serializers import ValidationError


class UrlValidator:
    """Класс валидатор для поля ссылки."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Метод для проверки допустимой ссылки"""
        if 'youtube.com' not in value:
            raise ValidationError('Должна быть ссылка с сайта "youtube.com"')
