from rest_framework import viewsets
from .models import TechnicalIndicator
from .serializers import TechnicalIndicatorSerializer

class TechnicalIndicatorViewSet(viewsets.ModelViewSet):
    queryset = TechnicalIndicator.objects.all()
    serializer_class = TechnicalIndicatorSerializer
