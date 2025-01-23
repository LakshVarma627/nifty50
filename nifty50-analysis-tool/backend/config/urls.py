from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.apps.users.views import UserViewSet
from backend.apps.nifty_data.api.routers import router as nifty_data_router

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/nifty_data/', include(nifty_data_router.urls)),
    path('api/alerts/', include('backend.apps.alerts.urls')),
    path('api/analysis/', include('backend.apps.analysis.urls')),
]
