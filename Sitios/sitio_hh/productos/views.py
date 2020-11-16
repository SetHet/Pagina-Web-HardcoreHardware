from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
def search(request):

    list_categorias = Categoria.objects.all()
    list_productos = Producto.objects.all()

    return render(request, "productos/search.html", {'list_categorias':list_categorias, 'list_productos':list_productos})  