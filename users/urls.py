from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIViewSet, UserCreateAPIViewSet, UserRetrieveAPIViewSet, UserListAPIViewSet, \
    UserUpdateAPIViewSet, UserDestroyAPIViewSet, SetSubscribeAPIView, PaymentCreateAPIViewSet

app_name = UsersConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user-create/', UserCreateAPIViewSet.as_view(), name='user-create'),
    path('user-view/<int:pk>/', UserRetrieveAPIViewSet.as_view(), name='user-view'),
    path('user-list/', UserListAPIViewSet.as_view(), name='user-list'),
    path('user-update/<int:pk>/', UserUpdateAPIViewSet.as_view(), name='user-update'),
    path('user-delete/<int:pk>/', UserDestroyAPIViewSet.as_view(), name='user-delete'),

    path('payment/list/', PaymentListAPIViewSet.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIViewSet.as_view(), name='payment_create'),

    path('subscribe/', SetSubscribeAPIView.as_view(), name='set_subscribe'),
]
