from django.shortcuts import render

from .forms import CommentForm
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


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CommentForm()
    contex = {
        'form': form,
        'product': product,
    }

    return render(request, 'product_detail.html', contex)
