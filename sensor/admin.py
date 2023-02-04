from django.contrib import admin
from . models import Sensors
from .models import TempHumid
from .models import Room
from .models import PersonInCharge

# Register your models here.

admin.site.register(Sensors)
admin.site.register(TempHumid)
admin.site.register(Room)
admin.site.register(PersonInCharge)


