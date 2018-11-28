# Generated by Django 2.0.2 on 2018-02-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darkroom_app', '0002_auto_20180226_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightsensordata',
            name='sensor',
            field=models.TextField(default='light1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lightsensordata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]