from django.db import models

# Create your models here.
class Sensors(models.Model):
    
    SensorName = models.CharField(max_length=200, null = False, blank = False)
    person = models.CharField(max_length=200, null = False, blank = False)
    location = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.SensorName + ' ' + self.person + ' ' + self.location
    
class TempHumid(models.Model):
    
    
    tempvalue = models.IntegerField()
    humidval = models.IntegerField()
    sensor = models.ForeignKey(Sensors, blank=True, null =True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.name)
