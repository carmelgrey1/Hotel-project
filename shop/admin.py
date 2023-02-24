from .models import Category, Product
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'availability',
'available', 'created', 'updated']
    list_editable = ['price', 'availability', 'available']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)