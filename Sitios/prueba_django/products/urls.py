from django.urls import path
from .views import search, product

urlpatterns = [
    path('search/', search, name='search'),
    path('product/<str:pk_product>/', product, name='product'),
]