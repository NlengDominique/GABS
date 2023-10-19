from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .form import ProductForm

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products/list.html', context)

def register_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'products/add.html', {'form':form})
    


      