from rest_framework import serializers

from online_school.models import Course
from online_school.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Класс сериализатора курса."""
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'
