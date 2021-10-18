from django.contrib import admin
from .models import *

@admin.register(Product_size)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_size']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price']