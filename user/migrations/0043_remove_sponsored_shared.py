# Generated by Django 3.0.5 on 2020-06-09 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0042_auto_20200609_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsored',
            name='shared',
        ),
    ]
