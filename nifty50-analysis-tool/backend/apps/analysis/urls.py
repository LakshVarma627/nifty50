from django.urls import path
from .views import TechnicalIndicatorViewSet

urlpatterns = [
    path('technical_indicators/', TechnicalIndicatorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('technical_indicators/<int:pk>/', TechnicalIndicatorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
