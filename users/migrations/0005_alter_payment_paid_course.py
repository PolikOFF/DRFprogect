# Generated by Django 5.0.4 on 2024-04-17 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_school', '0001_initial'),
        ('users', '0004_alter_payment_paid_course_alter_payment_paid_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_course', to='online_school.course', verbose_name='оплаченный курс'),
        ),
    ]
