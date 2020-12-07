from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products import views as products_views
from products.models import Categoria

# Create your views here.
def home(request):
    return products_views.home(request, baseRequired())


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