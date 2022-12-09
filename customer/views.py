from django.shortcuts import render
from product.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'customer/home.html', context)

