from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def prod_list(request, category_id=None):
    category =None
    products = Product.objcets.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products= Products.objects.filter(category=category, available=True)
    return render(request, 'shop/category.html', {'category':category, 'prods':products})