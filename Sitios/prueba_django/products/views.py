from django.shortcuts import render
from .models import Categoria, Producto
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def search(request):
    
    dicc = {}

    if (request.method == 'GET'):

        #Filtros
        categoriaFiltro = ""
        wordsFiltro = []

        # Separar el request.get en grupos
        groups = GetWordGroupsSearch(request)

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

        # Se filtra la busqueda en la BD
        query = BusquedaFiltrada(wordsFiltro, categoriaFiltro)

        # Se rescatan las categorias y productos seleccionados para enviarlos
        list_productos = query
        try:
            categoria_select = Categoria.objects.get(title__iexact=categoriaFiltro)
            dicc['categoria_select'] =  categoria_select
        except:
            pass
    else:
        # Se rescatan todas los productos para enviarlos si no hay filtro
        list_productos = Producto.objects.all()

    # Start Paginacion
    page = request.GET.get('page', 1)
    paginator = Paginator(list_productos, 12)
    
    try:
        list_productos = paginator.page(page)
    except PageNotAnInteger:
        list_productos = paginator.page(1)
    except EmptyPage:
        list_productos = paginator.page(paginator.num_pages)

    # End Paginacion

    dicc['list_productos'] = list_productos

    return render(request, "products/search.html", dicc)  


def GetWordGroupsSearch(request):
    # Conseguir el diccionario de la sentencia de busqueda
    searchDicc = request.GET

    # Revisar si tiene en el diccionario la key 'search'
    if 'search' in searchDicc:
        # Separar el valor de search en grupos
        groups = searchDicc['search'].split(' ')
    else:
        # Si no existe search se crea un grupo vacio
        groups = []

    return groups


def BusquedaFiltrada(wordsFiltro, categoriaFiltro):
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

    return query







def product(request, pk_product):
    dicc = {}
    dicc['producto'] = Producto.objects.get(id=pk_product)

    #money
    price = dicc['producto'].price
    money = str(int(price)) + " CLP"
    dicc['money'] = money

    return render(request, "products/product.html", dicc)