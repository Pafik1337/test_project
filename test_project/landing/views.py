from django.shortcuts import render
from .forms import SubscribersForm

# Create your views here.
def landing(request):
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request, 'landing/landing.html',locals())