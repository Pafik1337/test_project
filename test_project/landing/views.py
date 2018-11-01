from django.shortcuts import render
from .forms import SubscribersForm

# Create your views here.
def landing(request):
    form = SubscribersForm(request.POST or None)
    return render(request, 'landing/landing.html',locals())