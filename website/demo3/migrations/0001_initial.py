import os
from django.db import migrations
from django.utils import timezone


class Migration(migrations.Migration):
    dependencies = []  # can also be emtpy if it's your first migration

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD,
            last_login=timezone.now(),
        )

        superuser.save()

    operations = [

    ]
