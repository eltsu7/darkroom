from django.urls import path

from . import views
from .api import views as api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/sensors', api_views.light_sensor_get, name='api_sensors'),
    path('api/v1/sensors/latest', api_views.light_sensor_get_latest, name='api_sensors_latest'),    
    path('api/v1/sensors/post', api_views.light_sensor_post, name='api_sensors_post'),
    path('sensor_test', views.test, name='testi')
]