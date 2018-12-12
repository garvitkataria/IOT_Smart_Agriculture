# Generated by Django 2.1.2 on 2018-10-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_Type', '0005_auto_20181027_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='crop_type',
            field=models.CharField(choices=[('KC', 'Kharif crops'), ('RC', 'Rabi Crops'), ('ZC', 'Zaid Crop'), ('R', 'Rice'), ('W', 'Wheat'), ('P', 'Pulses'), ('SC', 'Sugarcane'), ('CT', 'Cotton'), ('GN', 'Groundnut'), ('T', 'Tea'), ('CF', 'Coffee')], default='P', max_length=20),
        ),
    ]
