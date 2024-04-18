from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentListAPIViewSet(generics.ListAPIView):
    """Класс для отображения списка Payment."""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ['payment_method', ]


class UserCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания User."""
    serializer_class = UserSerializer


class UserRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс для отображения User."""
    serializer_class = UserSerializer


class UserListAPIViewSet(generics.ListAPIView):
    """Класс для отображения списка User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс для обновления User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс для удаления User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
