import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AccessSim.settings')
django.setup()

from origin.models import Origin

DEFAULT_ORIGINS = [
    'Pesquisa Google',
    'Mídia Social',
    'Amigo ou Conhecido',
    'Anúncio',
    'Outro',
]

for name in DEFAULT_ORIGINS:
    Origin.objects.get_or_create(origin_name=name)

print('Origins seeded successfully.')
