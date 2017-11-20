from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from schedule.models import SchoolSubject
from schedule.utilities.serializers import SchoolSubjectSerializer


@csrf_exempt
def getAllSchoolSubjects(request):
    if request.method == 'GET':
        schoolSubjects = SchoolSubject.objects.all()
        serializer = SchoolSubjectSerializer(schoolSubjects, many=True)

        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getSchoolSubjectById(request, pk):
    try:
        schoolSubject = SchoolSubject.objects.get(pk=pk)
    except SchoolSubject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SchoolSubjectSerializer(schoolSubject)

        return JsonResponse(serializer.data)

@csrf_exempt
def createSchoolSubject(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SchoolSubjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def updateSchoolSubject(request, pk):
    try:
        schoolSubject = SchoolSubject.objects.get(pk=pk)
    except SchoolSubject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SchoolSubjectSerializer(schoolSubject, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def deleteSchoolSubject(request, pk):
    try:
        schoolSubject = SchoolSubject.objects.get(pk=pk)
    except SchoolSubject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        schoolSubject.delete()
        return HttpResponse(status=204)
