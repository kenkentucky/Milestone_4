# Create your views here.
from django.http import JsonResponse
from .serializers import SensorSerializer
from .serializers import TempHumidSerializer
from .serializers import RoomSerializer
from .serializers import PersonSerializer
from .models import Sensors
from .models import TempHumid
from .models import Room
from .models import PersonInCharge
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
@api_view(['GET','POST'])
def sensor_list(request, format = None):
    
    if request.method == 'GET':
        sensor= Sensors.objects.all()
        serializer = SensorSerializer(sensor, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def sensor_detail(request,id):
    
    try:
        sensor = Sensors.objects.get(pk=id)
    except Sensors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def sensor_value(request,format = None ):

    if request.method == 'GET':
        value= TempHumid.objects.all()
        serializer = TempHumidSerializer(value, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=TempHumidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

def dashboard(request):
    values = TempHumid.objects.all
    return render(request,"dashboard.html",{'values': values})

def home (request):
    return render(request, 'base.html')


@api_view(['GET','POST'])
def roomlist(request, format = None):
    
    if request.method == 'GET':
        room= Room.objects.all()
        serializer = RoomSerializer(room,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def personlist(request, format = None):
    
    if request.method == 'GET':
        sensor= PersonInCharge.objects.all()
        serializer = PersonSerializer(sensor, many = True)
        return Response(serializer.data)
        

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


def sensordashboard(request):
    values = Sensors.objects.all()
    return render(request,"dashboardsensor.html",{'values': values})



    
