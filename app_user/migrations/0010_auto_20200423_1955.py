# Generated by Django 3.0.5 on 2020-04-23 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0009_appuser_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='community',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='gender',
        ),
    ]
