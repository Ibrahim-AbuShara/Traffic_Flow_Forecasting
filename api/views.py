from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Sensor
from .serializers import SensorSerializer

@api_view(["GET"])
def get_sensors(request):
    sensor=Sensor.objects.all()
    serializer=SensorSerializer(sensor,many=True)
    return Response(serializer.data)