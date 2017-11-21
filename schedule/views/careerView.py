from rest_framework import viewsets
from schedule.models import Career
from schedule.utilities.serializers import CareerSerializer


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
