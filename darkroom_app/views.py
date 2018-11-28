import random

from django.shortcuts import render
from django.http import HttpResponse

from darkroom_app.models import SensorData

# Create your views here.
def index(request):
    entry = SensorData.objects.all().order_by('-datetime')[0]
    treshold = 200
    darkroom_open = entry.value > treshold
    context = {'darkroom_open' : darkroom_open}
    return render(request, 'darkroom_app/index.html', context)

def test(request):
    sensors = ['light1', 'door1']
    entry = SensorData(value=random.randint(0,1023), sensor=sensors[random.randint(0, len(sensors)-1)])
    entry.save()
    return HttpResponse('Success '+str(entry.value)+' '+str(entry.sensor))