from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products import views as products_views

# Create your views here.
def home(request):
    return products_views.home(request)

@login_required
def guias(request):
    return render(request, "core/guias.html")    

@login_required
def about(request):
    return render(request, "core/acerca_de.html")   

@login_required
def valorMoneda(request):
    return render(request, "core/calcular_precio.html") 
def login(request):
    return render(request, "core/login.html")