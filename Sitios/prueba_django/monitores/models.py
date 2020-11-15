from django.db import models

# Create your models here.
class Monitor(models.Model):
    tittle = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="monitores")
    price = models.CharField(max_length=50,verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"
        ordering = ['-created']
    def __str__(self):
        return self.tittle    