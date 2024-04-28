from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from online_school.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """Тест для CRUD уроков."""

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

    def test_create_lesson(self):
        """Тест на создание урока."""

        # Невалидные данные
        data = {
            'name': 'test',
            'video_url': 'google.com',
            'description': 'test1',
        }

        response = self.client.post('/lesson/create/', data=data)

        self.assertEqual(
            response.json(),
            {'video_url': ['Введите правильный URL.']}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertFalse(Lesson.objects.all().exists())

        # Валидные данные
        data = {
            'id': 1,
            'name': 'test',
            'video_url': 'https://www.youtube.com/watch?v=test',
        }

        response = self.client.post('/lesson/create/', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'name': 'test',
                'description': None,
                'preview': None,
                'video_url': 'https://www.youtube.com/watch?v=test',
                'course': None,
                'owner': 1,
            }
        )

        self.assertTrue(Lesson.objects.all().exists())

    def test_read_lesson_list(self):
        """Тест на чтение данных списка уроков."""
        lesson = Lesson.objects.create(
            name='Present Simple',
            owner=self.user
        )

        response = self.client.get('/lesson/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': lesson.pk,
                        'name': lesson.name,
                        'description': None,
                        'preview': None,
                        'video_url': None,
                        'course': None,
                        'owner': 3
                    }
                ]
            }
        )

    def test_read_lesson_retrieve(self):
        """Тест на чтение данных урока по его pk."""
        lesson = Lesson.objects.create(
            name='Present Simple',
            owner=self.user
        )

        response = self.client.get(f'/lesson/{lesson.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 4,
                'name': 'Present Simple',
                'description': None,
                'preview': None,
                'video_url': None,
                'course': None,
                'owner': 4
            }
        )

    def test_update_lesson(self):
        """Тест на обновление данных урока."""
        lesson = Lesson.objects.create(
            name='Present Simple',
            owner=self.user
        )

        data = {'name': 'Present Continuous'}

        response = self.client.patch(f'/lesson/update/{lesson.id}/', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 5,
                'name': 'Present Continuous',
                'description': None,
                'preview': None,
                'video_url': None,
                'course': None,
                'owner': 5
            }
        )

    def test_delete_lesson(self):
        """Тест на удаление урока."""
        lesson = Lesson.objects.create(
            name='Present Simple',
            owner=self.user
        )

        response = self.client.delete(f'/lesson/delete/{lesson.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
