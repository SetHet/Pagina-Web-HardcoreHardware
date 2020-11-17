"""prueba_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from monitores import views as monitores_views
from products import views as products_views
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('search/', products_views.search, name='search'),
    path('guias/', core_views.guias, name='guias'),
    path('monitores/',monitores_views.monitor, name='monitores'),
    path('about/', core_views.about, name='about'),
    path('calcularPrecio/', core_views.valorMoneda, name='valor_moneda'),
    path('login/', core_views.login, name='login'),
]
if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    