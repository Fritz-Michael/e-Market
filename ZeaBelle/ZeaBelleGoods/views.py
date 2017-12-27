from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from ZeaBelleGoods.forms import *

class HomeView(View):

	def get(self, request):
		items = Products.objects.all()
		return render(request,'home.html',{'items':items})


class ProductsView(View):

	def get(self, request):
		items = Products.objects.all()
		return render(request,'productlist.html',{'items':items})


class AddProductView(View):

	def get(self, request):
		form = AddNewProductForm()
		return render(request,'addproducts.html',{'form':form})

	def post(self, request):
		add_product_form = AddNewProductForm(request.POST,request.FILES)
		
		if add_product_form.is_valid():
			print('Valid form')
			temp = add_product_form.save(commit=False)
			temp.save()
		else:
			print('Inalid form')
			print(add_product_form.errors.as_data())		
		return redirect('ZeaBelleGoods:addproduct')