# Generated by Django 3.0.5 on 2020-05-01 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0018_auto_20200502_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='firebase_id',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),

    ]
