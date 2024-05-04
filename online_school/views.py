from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from online_school.models import Course, Lesson
from online_school.pagination import CustomPagination
from online_school.serializers.course import CourseSerializer
from online_school.serializers.lesson import LessonSerializer
from online_school.tasks import send_message_for_update
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с Course.
    Create, Update, Retrieve, Delete.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """Метод для привязки пользователя к созданному объекту."""
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """Метод для запуска функции отправки сообщения, при изменении курса."""
        update_course = serializer.save()
        send_message_for_update.delay(update_course.id)
        update_course.save()

    def get_permissions(self):
        """
        Функция для запрета действий по permissions.
        IsAuthenticated - проверка на авторизацию.
        IsModerator - проверка на принадлежность к модератору.
        """
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        # elif self.action == 'update':
        #     self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
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
    pagination_class = CustomPagination


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
