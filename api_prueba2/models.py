from django.db import models

class restaurante (models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(blank= True)
    precio = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    entrega = models.BooleanField(default=False)