# Generated by Django 2.0.2 on 2018-03-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darkroom_app', '0004_auto_20180226_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
