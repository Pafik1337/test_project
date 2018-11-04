from django.contrib import admin
from .models import *

class SubscriberAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields] # отоброжение всех полей в админке
    # list_filter = ["name"] # фильт в админке если есть много записей с одним именем 
    # search_fields = ["name","email"] # тоже фильтр, но писать самому
    # fields = [] # что показывать
    # exclude = ["email"] # что НЕ показывать
    # inlines = [] # встроеная форма в админке
    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)