import random
from datetime import datetime, timedelta

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from darkroom_app.models import SensorData
#from darkroom_app.rrd import rrd
from django.db.models import Min
from django.views.decorators.cache import cache_page

def light_sensor_entries_to_json(entries):
    response = {'entries' : []}
    for entry in entries:
        response['entries'].append({'value' : entry.value, 'inserted' : entry.datetime, 'sensor' : entry.sensor})

    return response

def valid_token(token):
    return token == 'ebin'

@cache_page(60)
def light_sensor_get(request):
    entries = SensorData.objects.all().order_by('-datetime')
    response = light_sensor_entries_to_json(entries)

    return JsonResponse(response)

@cache_page(30)
def light_sensor_get_latest(request):
    # Purkkaviritelmä koska SQLite ei tue DISTINCT ON kysel

    # Haetaan vain vuorokautta uudemmat tiedot, lisätään jokaiselta sensorilta
    #   ensimmäinen (uusin) arvo palautukseen.
    time_threshold = datetime.now() - timedelta(hours=24)
    entries_raw = SensorData.objects.filter(datetime__gt=time_threshold).order_by('-datetime')
    entry_sensors = []
    entries = []
    for entry in entries_raw:
        if entry.sensor not in entry_sensors:
            entries.append(entry)
            entry_sensors.append(entry.sensor)

    response = light_sensor_entries_to_json(entries)

    return JsonResponse(response)

def light_sensor_post(request):
    try:
        value = int(request.GET.get('value'))
        sensor = request.GET.get('sensor')
        token = request.GET.get('token')
    except ValueError:
        return HttpResponseBadRequest()

    if (value is not None) and valid_token(token):
        entry = SensorData(value=value, sensor=sensor)
        entry.save()
        #rrd.update(sensor, value)
        return HttpResponse('Success '+str(entry.value))
    else:
        return HttpResponseForbidden()