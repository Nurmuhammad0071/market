
# Url imports
from django.urls import path
from .views import products_list
# url ulr patterns
urlpatterns = [
    path('products_list/', products_list, name='products_list'),
    ]