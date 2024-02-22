from django.shortcuts import render

from product.models import Product


# Create your views here.
def products_list(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product_list.html', context)  # This is the view function
