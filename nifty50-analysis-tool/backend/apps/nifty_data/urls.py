from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyTimeSeriesViewSet, WeeklyTimeSeriesViewSet, MonthlyTimeSeriesViewSet

router = DefaultRouter()
router.register(r'daily', DailyTimeSeriesViewSet)
router.register(r'weekly', WeeklyTimeSeriesViewSet)
router.register(r'monthly', MonthlyTimeSeriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
