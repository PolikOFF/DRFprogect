from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, verbose_name='электронная почта', unique=True)
    phone = models.IntegerField(verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Email - {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'наличные'),
        ('card', 'банковский перевод')
    ]

    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='пользователь')
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')
    paid_course = models.ForeignKey('online_school.Course', on_delete=models.CASCADE, verbose_name='оплаченный курс',
                                    **NULLABLE)
    paid_lesson = models.ForeignKey('online_school.Lesson', on_delete=models.CASCADE, verbose_name='оплаченный урок',
                                    **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма платежа')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, default='card',
                                      verbose_name='метод оплаты')

    def __str__(self):
        return f'Пользователь - {self.user}\nДоступные курсы - {self.paid_course}\nДоступные уроки - {self.paid_lesson}.'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
