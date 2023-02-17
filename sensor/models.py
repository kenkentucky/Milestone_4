from django.db import models
from django.utils import timezone
# Create your models here.


class Sensors(models.Model):
    
    name = models.CharField(max_length=30, null = True, blank = False)
    PIC = models.CharField(max_length=30, null = True, blank = False)
    room = models.CharField(max_length=30, null =True, blank=False)
    
    def __str__(self):
        return self.name


class SensorData(models.Model):
    
 
    sensor = models.ForeignKey(Sensors,blank=True, null =True, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, null = False, blank = False)
    value1 = models.CharField(max_length=30, null = False, blank = False)
    value2 = models.CharField(max_length=30, null = False, blank = False)
    reading_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.sensor)

