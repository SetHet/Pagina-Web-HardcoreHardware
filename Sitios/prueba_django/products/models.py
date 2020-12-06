from django.db import models

# Create your models here.
class Categoria(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    tags = models.TextField(null=True, verbose_name="Tags")
    nameSpanish = models.CharField(max_length=50, null=True, verbose_name="Nombre Visible") 
    image = models.ImageField(upload_to="categorias", null=True, verbose_name="Imagen")
    background = models.ImageField(upload_to="categoriasBackGround", null=True, verbose_name="Imagen Fondo")

    def __str__(self):
        return self.title

class Producto(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to="productos")

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    price = models.FloatField()

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Informacion de producto"
        verbose_name_plural = "Informacion de productos"
        ordering = ['categoria' ,'name', '-update']

    def __str__(self):
        return self.categoria.title + " " + self.name