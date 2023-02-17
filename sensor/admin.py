from django.contrib import admin
from . models import Sensors
from .models import SensorData


# Register your models here.

admin.site.register(Sensors)
admin.site.register(SensorData)



