# Create your views here.

from .models import Sensors
from .models import SensorData


from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request,"base.html")



    
