from django.urls import path

from online_school.apps import OnlineSchoolConfig
from rest_framework.routers import DefaultRouter

from online_school.views import CourseViewSet, LessonCreateAPIViewSet, LessonListAPIViewSet, LessonRetrieveAPIViewSet, \
    LessonUpdateAPIViewSet, LessonDestroyAPIViewSet

app_name = OnlineSchoolConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIViewSet.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListAPIViewSet.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIViewSet.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>', LessonUpdateAPIViewSet.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIViewSet.as_view(), name='lesson_delete'),
] + router.urls
