from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home/index.html')


def product(request):
    product = Product.objects.all()
    contaxt = {
        'product': product,
    }
    return render(request, 'home/product.html', contaxt)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def accaunt(request):
    return render(request, 'home/accaunt.html')


def card(request):
    return render(request, 'home/card.html')


def product_details(request, pk):
    product_view = Product.objects.all()
    product = Product.objects.get(id=pk)
    contaxt = {
        'product_view':product_view,
        'product': product,
    }
    return render(request, 'home/product_details.html', contaxt)
