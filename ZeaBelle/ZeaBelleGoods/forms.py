from django import forms
from ZeaBelleGoods.models import *

class AddNewProductForm(forms.ModelForm):
	name = forms.CharField()
	unit_price = forms.DecimalField()
	retail_price = forms.DecimalField()
	quantity = forms.DecimalField()
	description = forms.CharField()
	thumbnail = forms.FileField()

	class Meta:
		model = Products
		fields = ['name','unit_price','retail_price','quantity','description','thumbnail']

class EditProductForm(forms.ModelForm):
	name = forms.CharField()
	unit_price = forms.DecimalField()
	retail_price = forms.DecimalField()
	quantity = forms.DecimalField()
	description = forms.CharField()
	thumbnail = forms.FileField()

	class Meta:
		model = Products
		fields = ['name','unit_price','retail_price','quantity','description','thumbnail']