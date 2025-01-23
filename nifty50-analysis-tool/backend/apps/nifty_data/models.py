from django.db import models
from polymorphic.models import PolymorphicModel

class TimeSeriesModel(PolymorphicModel):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()

    class Meta:
        abstract = True

class DailyTimeSeries(TimeSeriesModel):
    pass

class WeeklyTimeSeries(TimeSeriesModel):
    pass

class MonthlyTimeSeries(TimeSeriesModel):
    pass
