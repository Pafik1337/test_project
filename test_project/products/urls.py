from django.conf.urls import include, url
#form django.contrib import admin
from products import views

from . import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]
