from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def product(request):
    return render(request, 'home/product.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def accaunt(request):
    return render(request, 'home/accaunt.html')

def card(request):
    return render(request, 'home/card.html')