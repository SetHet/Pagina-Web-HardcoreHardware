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

    list_productos = list_productos.order_by('name')
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

    #Diccionario de precios
    dict_price = {}
    for producto in list_productos:
        dict_price[producto.id] = GetCLP(producto.price)
    
    dicc['dict_price'] = dict_price

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
    
    #producto elegido
    dicc['producto'] = Producto.objects.get(id=pk_product)

    #money
    price = dicc['producto'].price
    money = GetCLP(price)
    dicc['money'] = money

    #Enviar
    return render(request, "products/product.html", dicc)


def GetCLP(price):
    grupos_centenas = []
    string = str(int(price))

    #separar el numero en grupos
    while len(string) > 3:
        grupos_centenas.append(string[-3:])
        string = string[0:-3]
    grupos_centenas.append(string)

    #unir los grupos con puntos
    numero_unido = ""
    for centenar in reversed(grupos_centenas):
        numero_unido += centenar + "."

    numero_unido = numero_unido[0:-1]   

    #agregar contenido extra
    money_clp = "$ "+ numero_unido + " CLP"

    return money_clp