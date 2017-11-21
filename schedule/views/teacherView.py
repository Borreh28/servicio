from rest_framework import viewsets
from schedule.models import Teacher
from schedule.utilities.serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
