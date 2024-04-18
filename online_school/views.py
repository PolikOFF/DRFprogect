from rest_framework import viewsets, generics

from online_school.models import Course, Lesson
from online_school.serializers.course import CourseSerializer
from online_school.serializers.lesson import LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с Course.
    Create, Update, Retrieve, Delete.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Lesson."""
    serializer_class = LessonSerializer


class LessonListAPIViewSet(generics.ListAPIView):
    """Класс для просмотра списка Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс для просмотра Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс для обновления Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс для удаления Lesson."""
    queryset = Lesson.objects.all()
