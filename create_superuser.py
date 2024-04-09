import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from django.contrib.auth.models import User

# Substitua os valores abaixo conforme necessário
USERNAME = 'admin'
EMAIL = 'pulo@gmail'
PASSWORD = '1122'

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print('Superuser created successfully.')
else:
    print('Superuser creation skipped: already exists.')
