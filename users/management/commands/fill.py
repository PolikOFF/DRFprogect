import datetime

from django.core.management import BaseCommand

from online_school.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        Payment.objects.all().delete()

        user1, created = User.objects.get_or_create(email='test1@mail.ru')
        user2, created = User.objects.get_or_create(email='test2@mail.ru')

        course1, created = Course.objects.get_or_create(name='Course1')
        course2, created = Course.objects.get_or_create(name='Course2')

        lesson1, created = Lesson.objects.get_or_create(name='Lesson1', course=course1)
        lesson2, created = Lesson.objects.get_or_create(name='Lesson2', course=course2)

        payment1 = Payment.objects.create(
            user=user1,
            date_of_payment=datetime.datetime.now().date(),
            payment_amount=100000,
            payment_method='cash',
            paid_course=course1,
        )

        payment2 = Payment.objects.create(
            user=user2,
            date_of_payment=datetime.datetime.now().date(),
            payment_amount=150000,
            payment_method='card',
            paid_lesson=lesson1,
        )

        payment3 = Payment.objects.create(
            user=user1,
            date_of_payment=datetime.datetime.now().date(),
            payment_amount=50000,
            payment_method='card',
            paid_lesson=lesson2,
        )
