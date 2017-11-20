from rest_framework import serializers
from schedule.models import *


class TeacherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Teacher
		fields = '__all__'

class SchoolSubjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = SchoolSubject
		fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Career
		fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
	 
	 class Meta:
	 	model = Profile 
	 	fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Schedule 
		fields = '__all__'

class SchoolSubjectLogSerializer(serializers.ModelSerializer):

	class Meta:
		model = SchoolSubjectLog
		fields = '__all__'