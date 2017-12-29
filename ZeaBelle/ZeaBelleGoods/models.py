from django.db import models
from django.urls import reverse

# Create your models here.

class Products(models.Model):

	name = models.CharField(max_length=50)
	unit_price = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=3)
	retail_price = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=3)
	date_added = models.DateTimeField(auto_now=True)
	quantity = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=0)
	description = models.CharField(max_length=200,blank=True)
	thumbnail = models.ImageField(blank=True,null=True)

	def get_absolute_url(self):
		return reverse('ZeaBelleGoods:producttable')

	def __str__(self):
		return self.name