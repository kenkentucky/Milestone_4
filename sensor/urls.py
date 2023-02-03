from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('sensor/',views.sensor_list),
    path('sensor/<int:id>',views.sensor_detail),
    path('sensor-value/',views.sensor_value),
    path('dashboard/',views.dashboard),

]

urlpatterns = format_suffix_patterns(urlpatterns)
# path('',views.apiOverview, name='apiOverview'),
   # path('sensor-list/',views.showAll,name='sensor-list'),
   # path('sensor-detail/<int:pk>/',views.ViewProduct,name='sensor-detail'),
    #path('sensor-create/',views.CreateProduct,name='sensor-create'),
    #path('sensor-value/<int:pk>',views.ViewValue,name='value-detail'),
    #path('input-value/',views.CreateValue,name='value-create')
