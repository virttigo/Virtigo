# Generated by Django 3.0.5 on 2020-06-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200606_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='revenue',
            field=models.IntegerField(null=True),
        ),
    ]