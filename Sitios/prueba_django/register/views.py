from django.shortcuts import render
from .models import Registro
# Create your views here.
def register(request):
    if request.method == "POST":
        rut = request.POST['rut']
        name = request.POST['name']
        username = request.POST['username']
        birthdate = request.POST['birthdate']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        comments = request.POST['comments']
        print(rut, name, username, birthdate, address, email, password, comments)
        user = Registro(rut=rut, name=name, username=username, birthdate=birthdate, address=address, email=email, password=password, comments=comments)
        user.save()
    return render(request, "register/register.html")    

# def save(request):
#     if request.POST == "POST":

