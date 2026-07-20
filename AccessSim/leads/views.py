from django.http import JsonResponse
from django.views.decorators.http import require_POST

from origin.models import Origin
from status.models import Status

from .forms import LeadForm
from .models import Leads


@require_POST
def submit_lead(request):
    form = LeadForm(request.POST)

    if form.is_valid():
        status, _ = Status.objects.get_or_create(status_name='Novo')
        origin = form.cleaned_data['origin']

        Leads.objects.create(
            lead_name=form.cleaned_data['lead_name'],
            email=form.cleaned_data['email'],
            telefone=form.cleaned_data['telefone'],
            lead_message=form.cleaned_data['lead_message'],
            status=status,
            origin=origin,
        )

        return JsonResponse({
            'success': True,
            'message': 'Lead cadastrado com sucesso!',
        })

    errors = {
        field: [error for error in error_list]
        for field, error_list in form.errors.as_data().items()
    }

    return JsonResponse({
        'success': False,
        'message': 'Há erros no formulário.',
        'errors': errors,
    }, status=400)
