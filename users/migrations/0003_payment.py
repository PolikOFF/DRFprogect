# Generated by Django 5.0.4 on 2024-04-15 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_school', '0001_initial'),
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='сумма платежа')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('card', 'банковский перевод')], default='card', max_length=100, verbose_name='метод оплаты')),
                ('paid_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_school.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_school.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
