# Generated by Django 3.0.5 on 2020-06-01 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Phone_number',
            new_name='phone_number',
        ),
    ]
