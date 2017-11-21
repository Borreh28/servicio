from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from schedule.views import teacherView, schoolSubjectView, careerView, profileView, scheduleView

router = routers.SimpleRouter()
router.register(r'teachers', teacherView.TeacherViewSet)
router.register(r'subjects', schoolSubjectView.SchoolSubjectViewSet)
router.register(r'careers', careerView.CareerViewSet)
router.register(r'profiles', profileView.ProfileViewSet)
router.register(r'schedules', scheduleView.ScheduleViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
