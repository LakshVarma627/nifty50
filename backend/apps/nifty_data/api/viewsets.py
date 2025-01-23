from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from backend.apps.nifty_data.models import DailyTimeSeries, WeeklyTimeSeries, MonthlyTimeSeries
from backend.apps.nifty_data.api.serializers import DailyTimeSeriesSerializer, WeeklyTimeSeriesSerializer, MonthlyTimeSeriesSerializer

class DailyTimeSeriesViewSet(viewsets.ModelViewSet):
    queryset = DailyTimeSeries.objects.all()
    serializer_class = DailyTimeSeriesSerializer

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        return Response(serializer.data)

    def perform_bulk_create(self, serializer):
        DailyTimeSeries.objects.bulk_create(serializer.validated_data)

class WeeklyTimeSeriesViewSet(viewsets.ModelViewSet):
    queryset = WeeklyTimeSeries.objects.all()
    serializer_class = WeeklyTimeSeriesSerializer

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        return Response(serializer.data)

    def perform_bulk_create(self, serializer):
        WeeklyTimeSeries.objects.bulk_create(serializer.validated_data)

class MonthlyTimeSeriesViewSet(viewsets.ModelViewSet):
    queryset = MonthlyTimeSeries.objects.all()
    serializer_class = MonthlyTimeSeriesSerializer

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        return Response(serializer.data)

    def perform_bulk_create(self, serializer):
        MonthlyTimeSeries.objects.bulk_create(serializer.validated_data)
