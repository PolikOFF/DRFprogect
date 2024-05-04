from rest_framework import serializers

from online_school.models import Course
from online_school.serializers.lesson import LessonSerializer
from users.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    """Класс сериализатора курса."""
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = serializers.SerializerMethodField()

    def get_lesson_count(self, object):
        """Метод для получения количества уроков входящих в курс."""
        return object.lesson_set.count()

    def get_subscribe(self, object):
        """Метод для показа наличия подписки у пользователя."""
        return Subscription.objects.filter(course=object, user=self.context['request'].user).exists()

    class Meta:
        model = Course
        fields = '__all__'
