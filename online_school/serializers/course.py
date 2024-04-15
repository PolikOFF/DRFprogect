from rest_framework import serializers

from online_school.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'
