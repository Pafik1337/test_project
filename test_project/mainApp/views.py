from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас есть во просы то обращайтесь по телефону', '+37113372281488' , 'example@inbox.lv']})
