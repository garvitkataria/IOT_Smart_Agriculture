# Generated by Django 2.1.2 on 2018-10-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_Type', '0003_auto_20181027_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='crop_type',
            field=models.CharField(choices=[('KC', 'Kharif crops'), ('RC', 'Rabi Crops'), ('ZC', 'Zaid Crop'), ('R', 'Rice'), ('W', 'Wheat'), ('P', 'Pulses'), ('SC', 'Sugarcane'), ('CT', 'Cotton'), ('GN', 'Groundnut'), ('T', 'Tea'), ('CF', 'Coffee')], default='1', max_length=20),
        ),
    ]
