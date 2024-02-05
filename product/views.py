from django.shortcuts import render
from .models import Category, Product


# Create your views here.
def index(request):
    category = Category.objects.filter(status=1)
    product = Product.objects.filter(status=1)
    contex = {
        'category': category,
        'product': product,
    }
    return render(request, 'index.html', contex)
