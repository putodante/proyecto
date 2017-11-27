from django.db import models

from apps.profesores.models import profesores


# Create your models here.

class Castigos(models.Model):
    tipo=models.CharField(max_length=30)
    duracion = models.IntegerField()

    def __str__(self):
        return '{} | {}mins'.format(self.tipo,self.duracion)


class Alumnos(models.Model):
    profesor = models.ForeignKey(profesores, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    fechaMatricula = models.DateField()
    castigos = models.ManyToManyField(Castigos, blank=True)
