from functools import wraps

from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from leads.forms import LeadForm
from leads.models import Leads
from origin.models import Origin
from status.models import Status

from .serializers import LeadSerializer, OriginSerializer, StatusSerializer


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead_form'] = LeadForm()
        return context


class LeadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leads.objects.select_related('status', 'origin').all()
    serializer_class = LeadSerializer
    permission_classes = [IsAdminUser]


class OriginViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Origin.objects.all().order_by('origin_name')
    serializer_class = OriginSerializer
    permission_classes = [IsAdminUser]


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all().order_by('status_name')
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        raise PermissionDenied

    return _wrapped_view


@method_decorator(superuser_required, name='dispatch')
class ProtectedSwaggerSchemaView(SpectacularAPIView):
    pass


@method_decorator(superuser_required, name='dispatch')
class ProtectedSwaggerUIView(SpectacularSwaggerView):
    pass
