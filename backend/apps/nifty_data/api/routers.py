from rest_framework.routers import DefaultRouter
from backend.apps.nifty_data.api.viewsets import DailyTimeSeriesViewSet, WeeklyTimeSeriesViewSet, MonthlyTimeSeriesViewSet

router = DefaultRouter()
router.register(r'daily', DailyTimeSeriesViewSet)
router.register(r'weekly', WeeklyTimeSeriesViewSet)
router.register(r'monthly', MonthlyTimeSeriesViewSet)
