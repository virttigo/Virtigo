# Generated by Django 3.0.5 on 2020-06-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('date', models.IntegerField()),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('full_decription', models.TextField()),
            ],
        ),
    ]
