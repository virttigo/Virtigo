# Generated by Django 3.0.5 on 2020-06-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20200608_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='good',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
