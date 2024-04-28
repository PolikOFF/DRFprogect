from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from online_school.models import Course
from users.models import User


class SubscriptionTestCase(APITestCase):
    """Тест для подписки."""

    def setUp(self):
        """Метод для предоставления тестового объекта."""
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.ru',
            password='test',
            is_superuser=True,
            is_staff=True,
        )
        # аутентификация клиента
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='test',
            owner=self.user
        )

    def test_subscriptions(self):
        """Тест на работу подписки."""
        data = {
            'user': self.user,
            'course_id': self.course.pk,
        }

        response = self.client.post('/users/subscribe/', data=data)

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'message': 'подписка добавлена'}
        )
