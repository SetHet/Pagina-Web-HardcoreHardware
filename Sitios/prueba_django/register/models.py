from django.db import models

# Create your models here.
class Registro(models.Model):
    rut = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    birthdate = models.DateField()
    address = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    comments = models.TextField()