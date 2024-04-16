from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from users.models import Payment
from users.serializers import PaymentSerializer


# class PaymentViewSet(viewsets.ModelViewSet):
#     serializer_class = PaymentSerializer
#     queryset = Payment.objects.all()
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
#     ordering_fields = ('date_of_payment',)


class PaymentListAPIViewSet(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ['payment_method',]
