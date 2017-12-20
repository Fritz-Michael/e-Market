from django.conf.urls import url, include
from django.contrib import admin
from ZeaBelleGoods.views import *

admin.autodiscover()
app_name = 'ZeaBelleGoods'
urlpatterns = [
    #url(r'^home', HomeView.as_view(), name='home'),
    url(r'^$', ProductsView.as_view(), name='home'),
    url(r'^addproducts/$', AddProductView.as_view(), name='Add Products'),
]