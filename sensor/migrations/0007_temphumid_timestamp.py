# Generated by Django 4.1.6 on 2023-02-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0006_alter_sensors_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='temphumid',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]