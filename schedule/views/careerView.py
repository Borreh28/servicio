from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from schedule.models import Career
from schedule.utilities.serializers import CareerSerializer


@csrf_exempt
def getAllCareers(request):
    if request.method == 'GET':
        careers = Career.objects.all()
        serializer = CareerSerializer(careers, many=True)

        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getCareerById(request, pk):
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CareerSerializer(career)

        return JsonResponse(serializer.data)

@csrf_exempt
def createCareer(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CareerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def updateCareer(request, pk):
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CareerSerializer(career, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def deleteCareer(request, pk):
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        career.delete()
        return HttpResponse(status=204)
