from rest_framework import serializers

from users.models import Payment, User, Subscription


class PaymentSerializer(serializers.ModelSerializer):
    """Класс сериализатор для платежа."""
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатор для пользователя."""
    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Класс сериализатор для подписки."""
    class Meta:
        model = Subscription
        fields = '__all__'
