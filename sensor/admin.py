from django.contrib import admin
from . models import SensorList
from .models import SensorData


# Register your models here.

admin.site.register(SensorList)
admin.site.register(SensorData)



