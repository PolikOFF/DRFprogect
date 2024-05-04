from DRFprogect.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from users.models import Subscription


@shared_task
def send_message_for_update(course_id):
    """Функция на отправку письма, при обновлении курса."""
    subs = Subscription.objects.filter(course=course_id)
    subject = 'Новое обновление!'
    message = 'На вашем курсе появилось обновление! Скорее посмотрите!'
    if subs:
        email_list = []
        for sub in subs:
            email_list.append(sub.user.email)
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=email_list,
            fail_silently=True
        )
