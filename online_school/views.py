from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from online_school.models import Course, Lesson
from online_school.serializers.course import CourseSerializer
from online_school.serializers.lesson import LessonSerializer
from users.permissions import IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с Course.
    Create, Update, Retrieve, Delete.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        Функция для запрета действий не авторизованного пользователя и не модератора.
        IsAuthenticated - проверка на авторизацию.
        IsModerator - проверка на принадлежность к модератору.
        """
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsModerator]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Lesson."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class LessonListAPIViewSet(generics.ListAPIView):
    """Класс для просмотра списка Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс для просмотра Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс для обновления Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс для удаления Lesson."""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]
