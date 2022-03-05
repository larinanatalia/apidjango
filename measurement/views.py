# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorInfoSerializer, \
    SensorDetailSerializer




class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class SensorChangeView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class SensorInfoView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer







