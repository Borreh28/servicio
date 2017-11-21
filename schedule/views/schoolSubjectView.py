from rest_framework import viewsets
from schedule.models import SchoolSubject
from schedule.utilities.serializers import SchoolSubjectSerializer


class SchoolSubjectViewSet(viewsets.ModelViewSet):
    queryset = SchoolSubject.objects.all()
    serializer_class = SchoolSubjectSerializer
