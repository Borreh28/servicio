from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns 
from schedule.views import teacherView, schoolSubjectView, careerView, profileView, scheduleView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Teacher end-points
    url(r'^api/teachers/$', teacherView.getAllTeachers),
    url(r'^api/teachers/(?P<pk>[0-9]+)$', teacherView.getTeacherById),
    url(r'^api/teachers/create/$', teacherView.createTeacher),
    url(r'^api/teachers/update/(?P<pk>[0-9]+)$', teacherView.updateTeacher),
    url(r'^api/teachers/delete/(?P<pk>[0-9]+)$', teacherView.deleteTeacher),
    # School Subject end-points
    url(r'^api/schoolsubjects/$', schoolSubjectView.getAllSchoolSubjects),
    url(r'^api/schoolsubjects/(?P<pk>[0-9]+)$', schoolSubjectView.getSchoolSubjectById),
    url(r'^api/schoolsubjects/create/$', schoolSubjectView.createSchoolSubject),
    url(r'^api/schoolsubjects/update/(?P<pk>[0-9]+)$', schoolSubjectView.updateSchoolSubject),
    url(r'^api/schoolsubjects/delete/(?P<pk>[0-9]+)$', schoolSubjectView.deleteSchoolSubject),
    # Career end-points
    url(r'^api/careers/$', careerView.getAllCareers),
    url(r'^api/careers/(?P<pk>[0-9]+)$', careerView.getCareerById),
    url(r'^api/careers/create/$', careerView.createCareer),
    url(r'^api/careers/update/(?P<pk>[0-9]+)$', careerView.updateCareer),
    url(r'^api/careers/delete/(?P<pk>[0-9]+)$', careerView.deleteCareer),
    # Profile end-points
    url(r'^api/profiles/$', profileView.getAllProfiles),
    # Schedule end-points
    url(r'^api/schedules/$', scheduleView.getAllSchedules),
]

urlpatterns = format_suffix_patterns(urlpatterns)
