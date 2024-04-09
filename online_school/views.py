from rest_framework import viewsets, generics

from online_school.models import Course, Lesson
from online_school.serializers.course import CourseSerializer
from online_school.serializers.lesson import LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIViewSet(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIViewSet(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIViewSet(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIViewSet(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
