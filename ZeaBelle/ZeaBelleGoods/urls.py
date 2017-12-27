from django.conf.urls import url, include
from django.contrib import admin
from ZeaBelleGoods.views import *

admin.autodiscover()
app_name = 'ZeaBelleGoods'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^productlist', ProductsView.as_view(), name='producttable'),
    url(r'^addproducts/$', AddProductView.as_view(), name='addproduct'),
]