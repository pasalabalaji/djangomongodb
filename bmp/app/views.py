from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

from .serializers import *
from .models import *


def index(request):
    return HttpResponse("working")

@csrf_exempt
def departmentAPI(request,id=0):
    if(request.method=="GET"):
       departments=department.objects.all()
       department_serializer=deptserializer(departments,many=True)
       return JsonResponse(department_serializer.data,safe=False)
    elif(request.method=="POST"):
        data=JSONParser().parse(request)
        department_serializer=deptserializer(data=data)
        department_serializer.is_valid(raise_exception=True)
        department_serializer.save()
        return JsonResponse(department_serializer.data,safe=False)