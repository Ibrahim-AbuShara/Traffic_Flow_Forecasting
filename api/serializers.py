from rest_framework import serializers
from base.models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields="__all__"