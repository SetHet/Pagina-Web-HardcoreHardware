from django.urls import path
from .views import home , guias, about, login, valorMoneda

urlpatterns = [
    
    path('', home, name='home'),
    path('guias/', guias, name='guias'),
    path('about/', about, name='about'),
    path('calcularPrecio/', valorMoneda, name='valor_moneda'),
    path('login/', login, name='login'),
    
]