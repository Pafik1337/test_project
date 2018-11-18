from django.shortcuts import render
from .forms import SubscribersForm
from products.models import *

# Create your views here.
def landing(request):
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request, 'landing/landing.html',locals())

def home(request):
    products_images = ProductImage.objects.filter(is_main = True, is_active = True, product__is_active = True)
    products_images_cactuses = products_images.filter(product__category__id = 1)
    products_images_bricks = products_images.filter(product__category__id = 2)
    return render(request, 'landing/home.html',locals())