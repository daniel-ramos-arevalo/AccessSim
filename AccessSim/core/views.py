from django.views.generic import TemplateView

from leads.forms import LeadForm


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead_form'] = LeadForm()
        return context
