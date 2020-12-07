from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products import views as products_views
from products.models import Categoria, Producto
import random

# Create your views here.
def home(request):

    dictionary_models = ProductosCarruselHome(baseRequired())

    return products_views.home(request, dictionary_models)


def guias(request):
    return render(request, "core/guias.html", baseRequired())    


def about(request):
    return render(request, "core/acerca_de.html", baseRequired())   


def valorMoneda(request):
    return render(request, "core/calcular_precio.html", baseRequired()) 

def login(request):
    return render(request, "core/login.html", baseRequired())


def baseRequired():
    dicctionary = {
        'categorias_all':Categoria.objects.all().order_by('nameSpanish')
    }

    return dicctionary



# Funciones

def ProductosCarruselHome(dictionary):

    cantidad_final = 16
    seleccionados_index = []
    all_products = Producto.objects.all()

    for ciclo in range(cantidad_final):
        #Encontrar uno random
        pos = random.randint(0, len(all_products) - 1)
        pos_random = pos
        if not pos in seleccionados_index:
            seleccionados_index.append(pos)
            continue
        #Buscar en el resto de la lista
        pos+=1
        while pos % len(all_products) != pos_random:
            new_pos = pos % len(all_products)
            if not new_pos in seleccionados_index:
                seleccionados_index.append(new_pos)
                break
            pos+=1
        if pos % len(all_products) != pos_random:
            continue
        #Tomar valor random aunque este repetido
        seleccionados_index.append(pos_random)

    #Almacenar productos seleccionados
    selected_products = []
    for index in seleccionados_index:
        selected_products.append(all_products[index])

    #Repartir
    list_productos_carrousel_1 = selected_products[0:4]
    list_productos_carrousel_2_1 = selected_products[4:7]
    list_productos_carrousel_2_2 = selected_products[7:10]
    list_productos_carrousel_3_1 = selected_products[10:13]
    list_productos_carrousel_3_2 = selected_products[13:16]

    dictionary["list_productos_carrousel_1"] = list_productos_carrousel_1
    dictionary["list_productos_carrousel_2_1"] = list_productos_carrousel_2_1
    dictionary["list_productos_carrousel_2_2"] = list_productos_carrousel_2_2
    dictionary["list_productos_carrousel_3_1"] = list_productos_carrousel_3_1
    dictionary["list_productos_carrousel_3_2"] = list_productos_carrousel_3_2

    return dictionary
        




