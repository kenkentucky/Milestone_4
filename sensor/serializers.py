from  rest_framework import serializers

from . models import Sensors
from . models import TempHumid
from .models import Room
from .models import PersonInCharge

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'
        
class TempHumidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHumid
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInCharge
        fields = '__all__'
