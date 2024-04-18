from django.urls import path

from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentListAPIViewSet, UserCreateAPIViewSet, UserRetrieveAPIViewSet, UserListAPIViewSet, \
    UserUpdateAPIViewSet, UserDestroyAPIViewSet

app_name = UsersConfig.name
#
# router = DefaultRouter()
# router.register(r'payments', PaymentViewSet, basename='courses')

urlpatterns = [
    path('user-create/', UserCreateAPIViewSet.as_view(), name='user-create'),
    path('user-view/<int:pk>/', UserRetrieveAPIViewSet.as_view(), name='user-view'),
    path('user-list/', UserListAPIViewSet.as_view(), name='user-list'),
    path('user-update/<int:pk>/', UserUpdateAPIViewSet.as_view(), name='user-update'),
    path('user-delete/<int:pk>/', UserDestroyAPIViewSet.as_view(), name='user-delete'),

    path('list/', PaymentListAPIViewSet.as_view(), name='payment_list'),
]  # + router.urls
