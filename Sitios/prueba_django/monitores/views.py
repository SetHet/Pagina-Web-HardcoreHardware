from django.shortcuts import render
from .models import Monitor
from django.contrib.auth.decorators import login_required
# Create your views here.


def monitor(request):
    monitores = Monitor.objects.all()
    return render(request, "monitores/monitores.html",{'monitores':monitores})