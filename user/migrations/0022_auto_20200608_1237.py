# Generated by Django 3.0.5 on 2020-06-08 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('user', '0021_auto_20200608_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='personal',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sub', models.CharField(choices=[('Personal', 'Personal'), ('..', '..')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sub',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sub1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sub2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sub3',
        ),
    ]
