from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    get_user_model().objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin',
    )


def drop_superuser(apps, schema_editor):
    apps.get_model(settings.AUTH_USER_MODEL).objects.filter(
        username='admin',
        email='admin@example.com',
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, drop_superuser)
    ]
