from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return HttpResponse("<h1>Sobre nosotros</h1><h2>Yoyoyos</h2>")


def calc(request):
    return render(request, "core/calc.html")
