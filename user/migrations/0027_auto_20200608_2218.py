# Generated by Django 3.0.5 on 2020-06-08 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_auto_20200608_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='share',
            old_name='values',
            new_name='value',
        ),
    ]