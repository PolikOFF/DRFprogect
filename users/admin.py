from django.contrib import admin

from users.models import User, Payment, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid_course', 'paid_lesson', 'payment_method')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
