from django import forms

from origin.models import Origin


class LeadForm(forms.Form):
    lead_name = forms.CharField(
        label='Nome *',
        max_length=150,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'placeholder': 'Nome Completo',
            'required': True,
        }),
    )
    email = forms.EmailField(
        label='Email *',
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'emailexemplo@gmail.com',
            'required': True,
        }),
    )
    telefone = forms.CharField(
        label='Telefone',
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            'id': 'phone',
            'placeholder': '(00) 00000-0000',
        }),
    )
    lead_message = forms.CharField(
        label='Mensagem',
        required=False,
        widget=forms.Textarea(attrs={
            'id': 'message',
            'rows': 4,
            'cols': 40,
        }),
    )
    origin = forms.ModelChoiceField(
        label='Como nos encontrou? *',
        queryset=Origin.objects.order_by('origin_name'),
        empty_label='Selecione uma opção',
        required=True,
        to_field_name='origin_id',
        widget=forms.Select(attrs={
            'id': 'origin',
            'required': True,
        }),
    )