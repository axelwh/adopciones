from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    # imagen = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos


class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
