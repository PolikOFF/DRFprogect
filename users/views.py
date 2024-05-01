from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from online_school.models import Course
from users.models import Payment, User, Subscription
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_product, create_stripe_session


class PaymentListAPIViewSet(generics.ListAPIView):
    """Класс для отображения списка Payment."""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ['payment_method', ]


class PaymentCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания платежа."""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        product = create_stripe_product(payment)
        price = create_stripe_price(payment.payment_amount, product)

        session_id, payment_id = create_stripe_session(price)
        payment.payment_id = session_id
        payment.payment_link = payment_id

        payment.save()


class UserCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания User."""
    serializer_class = UserSerializer


class UserRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс для отображения User."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserListAPIViewSet(generics.ListAPIView):
    """Класс для отображения списка User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс для обновления User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс для удаления User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class SetSubscribeAPIView(APIView):
    """Класс для установки/удаления подписки пользователя."""
    def post(self, *args, **kwargs):
        """Метод управления подпиской."""
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course_item = Course.objects.get(id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            # subs_item.create(user=user, course=course_item)
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})
