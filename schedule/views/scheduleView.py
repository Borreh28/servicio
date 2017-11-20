from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from schedule.models import Schedule
from schedule.utilities.serializers import ScheduleSerializer


@csrf_exempt
def getAllSchedules(request):
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)

        return JsonResponse(serializer.data, safe=False)
