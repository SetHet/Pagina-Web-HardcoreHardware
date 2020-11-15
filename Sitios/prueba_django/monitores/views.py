from django.shortcuts import render
from .models import Monitor
# Create your views here.
def monitor(request):
    monitores = Monitor.objects.all()
    return render(request, "monitores/monitores.html",{'monitores':monitores})