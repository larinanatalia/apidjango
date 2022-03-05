from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 60)


class Measurement(models.Model):
    sensors_id = models.ForeignKey(Sensor, on_delete = models.CASCADE, )
    temperature = models.IntegerField()
    measurement_data = models.DateField()
