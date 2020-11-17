from django.contrib import admin
from .models import Categoria
from .models import Producto

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Categoria)
admin.site.register(Producto, ProductosAdmin)