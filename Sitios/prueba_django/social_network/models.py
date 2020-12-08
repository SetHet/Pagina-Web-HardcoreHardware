from django.db import models

# Create your models here.
class SocialNetwork(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=50, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=100)
    url = models.URLField(verbose_name="Enlace web", max_length=300, null=True, blank=True)
    icon = models.SlugField(verbose_name="Icono FontAwesome", max_length=100, null=True)

    #Datos de modificaciones
    created = models.DateTimeField(verbose_name="Fecha Creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha Actualización", auto_now=True)

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ['name']

    def __str__(self):
        return self.key
