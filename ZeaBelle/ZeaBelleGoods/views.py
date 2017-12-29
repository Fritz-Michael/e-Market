from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from ZeaBelleGoods.forms import *
from ZeaBelleGoods.models import Products

class HomeView(View):

	def get(self, request):
		items = Products.objects.all()
		paginator = Paginator(items, 10)
		page = request.GET.get('page')
		query = request.GET.get("q")
		if query:
			items = items.filter(name__contains=query)
		try:
			all_items = paginator.page(page)
		except PageNotAnInteger:
			all_items = paginator.page(1)
		except EmptyPage:
			all_items = paginator.page(paginator.num_pages)
		return render(request,'home.html',{'items':items})


class ProductsView(View):

	def get(self, request):
		items = Products.objects.all()
		query = request.GET.get("q")
		form = EditProductForm()
		if query:
			items = items.filter(name__contains=query)
		return render(request,'productlist.html',{'items':items, 'form':form})

	def post(self, request):
		edit_product_form = EditProductForm(request.POST,request.FILES)
		if edit_product_form.is_valid():
			print('Valid form')
			temp = edit_product_form.save(commit=False)
			temp.save()
		else:
			print('Inalid form')
			print(edit_product_form.errors.as_data())		
		return redirect('ZeaBelleGoods:producttable')

class AddProductView(CreateView):

	form_class = AddNewProductForm
	template_name = 'addproducts.html'
	success_url = reverse_lazy('ZeaBelleGoods:addproduct')

	# def get(self, request):
	# 	form = AddNewProductForm()
	# 	return render(request,'addproducts.html',{'form':form})

	# def post(self, request):
	# 	add_product_form = AddNewProductForm(request.POST,request.FILES)
	# 	if add_product_form.is_valid():
	# 		print('Valid form')
	# 		temp = add_product_form.save(commit=False)
	# 		temp.save()
	# 	else:
	# 		print('Inalid form')
	# 		print(add_product_form.errors.as_data())		
	# 	return redirect('ZeaBelleGoods:addproduct')

class EditProductView(UpdateView):

	model = Products
	form_class = AddNewProductForm
	template_name = 'addproducts.html'
	#fields = ['name','unit_price','retail_price','quantity','description','thumbnail']
	success_url = reverse_lazy('ZeaBelleGoods:producttable')


class DeleteProductView(DeleteView):

	model = Products
	template_name = 'products_confirm_delete.html'
	success_url = reverse_lazy('ZeaBelleGoods:producttable')

	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)