# Generated by Django 3.0.5 on 2020-06-09 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0030_auto_20200609_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsored',
            name='shared',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shared', to=settings.AUTH_USER_MODEL),
        ),
    ]
