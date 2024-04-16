from django.urls import path

from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentListAPIViewSet

app_name = UsersConfig.name
#
# router = DefaultRouter()
# router.register(r'payments', PaymentViewSet, basename='courses')

urlpatterns = [
    path('list/', PaymentListAPIViewSet.as_view(), name='payment_list'),
]  # + router.urls
