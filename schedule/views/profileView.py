from rest_framework import viewsets
from schedule.models import Profile
from schedule.utilities.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
