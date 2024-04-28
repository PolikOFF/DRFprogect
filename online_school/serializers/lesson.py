from rest_framework import serializers

from online_school.models import Lesson
from online_school.validators import video_url_validator


class LessonSerializer(serializers.ModelSerializer):
    """Класс сериализатора урока."""
    video_url = serializers.CharField(validators=[video_url_validator], required=False)

    class Meta:
        model = Lesson
        fields = '__all__'
