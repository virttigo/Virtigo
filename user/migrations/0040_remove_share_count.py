# Generated by Django 3.0.5 on 2020-06-09 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20200609_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='count',
        ),
    ]