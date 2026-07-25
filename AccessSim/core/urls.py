from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    HomeView,
    LeadViewSet,
    OriginViewSet,
    ProtectedSwaggerSchemaView,
    ProtectedSwaggerUIView,
    StatusViewSet,
)

router = DefaultRouter()
router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'origins', OriginViewSet, basename='origin')
router.register(r'statuses', StatusViewSet, basename='status')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('api/schema/', ProtectedSwaggerSchemaView.as_view(), name='schema'),
    path('api/docs/', ProtectedSwaggerUIView.as_view(), name='swagger-ui'),
]