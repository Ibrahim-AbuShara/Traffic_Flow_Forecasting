from django.db import models

# Create your models here.
class Sensor(models.Model):
    sensor_id=models.CharField(max_length=10,primary_key=True)
    varimax_path=models.CharField(max_length=500)
    rfr_path=models.CharField(max_length=500)
    
    
