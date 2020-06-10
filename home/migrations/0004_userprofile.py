# Generated by Django 3.0.5 on 2020-06-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blogpost_full_decription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('tasks_completed', models.IntegerField()),
                ('referrals', models.IntegerField()),
                ('subcription', models.IntegerField()),
                ('revenue', models.IntegerField()),
                ('notif', models.TextField()),
            ],
        ),
    ]