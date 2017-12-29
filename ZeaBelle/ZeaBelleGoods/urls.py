from django.conf.urls import url, include
from django.contrib import admin
from ZeaBelleGoods.views import *

admin.autodiscover()
app_name = 'ZeaBelleGoods'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^productlist', ProductsView.as_view(), name='producttable'),
    url(r'^addproducts/$', AddProductView.as_view(), name='addproduct'),
    url(r'products/edit/(?P<pk>[0-9]+)/$', EditProductView.as_view(), name='edit-product'),
    url(r'products/delete/(?P<pk>[0-9]+)/$', DeleteProductView.as_view(), name='delete-product')
]