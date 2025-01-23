from django.urls import path
from .views import AlertRuleViewSet

urlpatterns = [
    path('alerts/', AlertRuleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('alerts/<int:pk>/', AlertRuleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
