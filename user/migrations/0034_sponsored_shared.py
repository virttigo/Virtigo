# Generated by Django 3.0.5 on 2020-06-09 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0033_remove_sponsored_shared'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsored',
            name='shared',
            field=models.ManyToManyField(blank=True, default=None, related_name='shared', to=settings.AUTH_USER_MODEL),
        ),
    ]
