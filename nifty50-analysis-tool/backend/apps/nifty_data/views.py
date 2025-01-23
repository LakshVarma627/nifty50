from rest_framework import viewsets
from .models import DailyTimeSeries, WeeklyTimeSeries, MonthlyTimeSeries
from .serializers import DailyTimeSeriesSerializer, WeeklyTimeSeriesSerializer, MonthlyTimeSeriesSerializer

class DailyTimeSeriesViewSet(viewsets.ModelViewSet):
    queryset = DailyTimeSeries.objects.all()
    serializer_class = DailyTimeSeriesSerializer

class WeeklyTimeSeriesViewSet(viewsets.ModelViewSet):
    queryset = WeeklyTimeSeries.objects.all()
    serializer_class = WeeklyTimeSeriesSerializer

class MonthlyTimeSeriesViewSet(viewsets.ModelViewSet):
    queryset = MonthlyTimeSeries.objects.all()
    serializer_class = MonthlyTimeSeriesSerializer
