# Generated by Django 3.0.5 on 2020-06-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_remove_personal_good'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sub',
            field=models.CharField(choices=[('Personal', 'Personal $1.99'), ('Business', 'Business $13'), ('Ultimate', 'Ultimate $39'), ('Premium', 'Premium $65')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='personal',
        ),
    ]
