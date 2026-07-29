from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import IntegrityError
from status.models import Status

from .forms import LeadForm
from .models import Leads

import re
import phonenumbers

def is_valid_phone(phone, region="BR"):
    try:
        parsed = phonenumbers.parse(phone, region)
        return phonenumbers.is_valid_number(parsed)
    except phonenumbers.NumberParseException:
        return False
    
def is_valid_email(email):
    pattern = r'\w+@\w+\.\w+'
    return re.match(pattern, email)

@require_POST
def submit_lead(request):
    form = LeadForm(request.POST)

    if not form.is_valid():
        if 'email' in form.errors:
            return JsonResponse({
                'success': False,
                'message': 'O email informado é inválido.',
            }, status=400)

        errors = {
            field: [str(error) for error in error_list]
            for field, error_list in form.errors.as_data().items()
        }

        return JsonResponse({
            'success': False,
            'message': 'Há erros no formulário.',
            'errors': errors,
        }, status=400)

    status, _ = Status.objects.get_or_create(status_name='Novo')
    origin = form.cleaned_data['origin']

    try:
        if not is_valid_phone(form.cleaned_data['telefone']):
            return JsonResponse({
                'success': False,
                'message': 'O telefone informado é inválido.',
            }, status=400)

        if not is_valid_email(form.cleaned_data['email']):
            return JsonResponse({
                'success': False,
                'message': 'O email informado é inválido.',
            }, status=400)

        Leads.objects.create(
            lead_name=form.cleaned_data['lead_name'],
            email=form.cleaned_data['email'],
            telefone=form.cleaned_data['telefone'],
            lead_message=form.cleaned_data['lead_message'],
            status=status,
            origin=origin,
        )

    except IntegrityError as exc:
        message = str(exc).lower()
        print(f"Database error: {message}")

        if 'email' in message and 'duplicate' in message:
            return JsonResponse({
                'success': False,
                'message': 'O email já está cadastrado.',
            }, status=400)

        return JsonResponse({
            'success': False,
            'message': 'Ocorreu um erro de comunicação com o servidor.',
        }, status=400)

    return JsonResponse({
        'success': True,
        'message': 'Lead cadastrado com sucesso.',
    })

