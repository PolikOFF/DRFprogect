from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from online_school.models import Course, Lesson
from online_school.serializers.course import CourseSerializer
from online_school.serializers.lesson import LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с Course.
    Create, Update, Retrieve, Delete.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        """Метод для привязки пользователя к созданному объекту."""
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        """
        Функция для запрета действий не авторизованного пользователя и не модератора.
        IsAuthenticated - проверка на авторизацию.
        IsModerator - проверка на принадлежность к модератору.
        """
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, ~IsModerator & IsOwner]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Lesson."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        """Метод для привязки курса к созданному объекту."""
        serializer.save(owner=self.request.user)


class LessonListAPIViewSet(generics.ListAPIView):
    """Класс для просмотра списка Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс для просмотра Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс для обновления Lesson."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс для удаления Lesson."""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator & IsOwner]
