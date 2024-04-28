from rest_framework import serializers

from online_school.models import Lesson
from online_school.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    """Класс сериализатора урока."""

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_url')]
