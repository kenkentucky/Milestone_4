from  rest_framework import serializers

from . models import Sensors
from . models import TempHumid

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'
        
class TempHumidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHumid
        fields = '__all__'
