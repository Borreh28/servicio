from rest_framework.serializers import ModelSerializer
from schedule.models import *


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SchoolSubjectSerializer(ModelSerializer):
    class Meta:
        model = SchoolSubject
        fields = '__all__'


class CareerSerializer(ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class SchoolSubjectLogSerializer(ModelSerializer):
    class Meta:
        model = SchoolSubjectLog
        fields = '__all__'
