from django.conf import settings
from django.db import models
from Farm.models import Farm


class Crop(models.Model):
	farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm')
	CROP_TYPES = (
        ('KC', 'Kharif crops'),
        ('RC', 'Rabi Crops'),
        ('ZC', 'Zaid Crop'),
        ('R', 'Rice'),
        ('W', 'Wheat'),
        ('P', 'Pulses'),
        ('SC', 'Sugarcane'),
        ('CT', 'Cotton'),
        ('GN', 'Groundnut'),
        ('T', 'Tea'),
        ('CF', 'Coffee')
    )
	crop_type = models.CharField(max_length=20, choices=CROP_TYPES, default='1')
	location = models.FloatField(default=0.00)
	latitude = models.FloatField(default=0.00)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)+'--'+ self.farm.__str__()+'--'+str(self.crop_type)