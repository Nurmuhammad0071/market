from django.urls import path

from product.views import index, product_detail, search

urlpatterns = [
    path('', index, name='index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('search/', search, name='search')
]
