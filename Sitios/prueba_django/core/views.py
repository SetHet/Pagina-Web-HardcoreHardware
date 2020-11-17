from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")
def guias(request):
    return render(request, "core/guias.html")    
def about(request):
    return render(request, "core/acerca_de.html")   
def valorMoneda(request):
    return render(request, "core/calcular_precio.html") 
def login(request):
    return render(request, "core/login.html")