from __future__ import unicode_literals

from django.db import models

from apps_adopciones.adopcion.models import Persona


# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, null=True)
    imagen = models.ImageField(upload_to='mascotas/', null=True, blank=True)

    def __str__(self):
        return self.nombre
