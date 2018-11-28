from django.db import models

# Create your models here.
class SensorData(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    value = models.IntegerField(blank=False)
    sensor = models.TextField(blank=False)