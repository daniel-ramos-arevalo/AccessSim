from django.test import TestCase

from origin.models import Origin

from .forms import LeadForm


class LeadFormTests(TestCase):
    def test_form_contains_expected_fields_and_labels(self):
        form = LeadForm()

        self.assertIn('lead_name', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('telefone', form.fields)
        self.assertIn('lead_message', form.fields)
        self.assertIn('origin', form.fields)
        self.assertEqual(form.fields['lead_name'].label, 'Nome *')
        self.assertEqual(form.fields['email'].label, 'Email *')
        self.assertEqual(form.fields['telefone'].label, 'Telefone')
        self.assertEqual(form.fields['lead_message'].label, 'Mensagem')
        self.assertEqual(form.fields['origin'].label, 'Como nos encontrou? *')

    def test_origin_field_uses_origin_model_queryset(self):
        origin = Origin.objects.create(origin_name='Pesquisa Google')
        form = LeadForm()

        self.assertIn(origin, form.fields['origin'].queryset)
