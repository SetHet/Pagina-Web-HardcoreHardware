from django.shortcuts import render, redirect   
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from .models import Contacto

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            emailv = EmailMessage(
                "HardcoreHardware: Contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no-reply@inbox.mailtrap.io",
                ["soportehardcorehardware@gmail.com"],
                reply_to = [email]
            )
            try:
                emailv.send()
                contacto = Contacto(name=name,email=email,content=content)
                contacto.save()
                return redirect(reverse('contact') + "?OK")
            except:
                return redirect(reverse('contact') + "?FAIL")
            return redirect(reverse('contact') + "?OK")
    return render(request,"contact/contact.html", {'form':contact_form})