from rest_framework import viewsets
from schedule.models import Schedule
from schedule.utilities.serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
