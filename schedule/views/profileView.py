from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from schedule.models import Profile
from schedule.utilities.serializers import ProfileSerializer


@csrf_exempt
def getAllProfiles(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)

        return JsonResponse(serializer.data, safe=False)
