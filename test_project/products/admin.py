from django.contrib import admin
from .models import *


class ProductCategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields] # отоброжение всех полей в админке
    class Meta:
        model = ProductCategory
admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0 # дополнительные ряды

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields] # отоброжение всех полей в админке
    inlines = [ProductImageInline]
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields] # отоброжение всех полей в админке
    class Meta:
        model = ProductImage
admin.site.register(ProductImage, ProductImageAdmin)
