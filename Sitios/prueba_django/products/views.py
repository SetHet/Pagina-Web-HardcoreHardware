from django.shortcuts import render
from .models import Categoria, Producto
from django.db.models import Q

# Create your views here.
def search(request):

    if (request.method == 'GET'):

        #Filtros
        categoriaFiltro = ""
        wordsFiltro = []

        # Conseguir el diccionario de la sentencia de busqueda
        searchDicc = request.GET

        # Revisar si tiene en el diccionario la key 'search'
        if 'search' in searchDicc:
            # Separar el valor de search en grupos
            groups = searchDicc['search'].split(' ')
        else:
            # Si no existe search se crea un grupo vacio
            groups = []

        # Revisar que el search no esta vacio
        if not (len(groups) == 1 and groups[0] == ""):
            # Guardar los filtros
            for grp in groups:
                comandos = grp.split(':')
                valor = comandos[0]
                # Si el filtro es complejo se analisa y determina si pertenece a una caracteristica especifica
                if len(comandos) > 1:
                    tag = comandos[0]
                    valor = comandos[1]
                    if tag.lower() == "categoria":
                        categoriaFiltro = valor
                        continue
                # Si no es un filtro complejo se guarda en palabras filtro
                wordsFiltro.append(valor)

        # Se comienza con un 'select * from producto;'
        query = Producto.objects.all()

        # Si existe filtro de categoria especifico se filtra para que solo pertenescan a esa categoria
        if categoriaFiltro != "":
            query = query.filter(categoria__title__iexact=categoriaFiltro)
        
        # Si hay palabras filtro se buscan todos los productos que contengan alguna de las palabras
        if len(wordsFiltro) > 0:
            query_original = query
            # primer filtro para tener una base
            query = query_original.filter(name__icontains=wordsFiltro[0]) 
            for word in wordsFiltro:
                query = query | query_original.filter(Q(name__icontains=word) | Q(descripcion__icontains=word) | Q(categoria__title__icontains=word))

        # Se rescatan las categorias y productos seleccionados para enviarlos
        list_categorias = Categoria.objects.all()
        list_productos = query
    else:
        # Se rescatan todas las categorias y productos para enviarlos si no hay filtro
        list_categorias = Categoria.objects.all()
        list_productos = Producto.objects.all()

    
    return render(request, "products/search.html", {'list_categorias':list_categorias, 'list_productos':list_productos})  