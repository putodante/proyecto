from django.db import models
from apps.materias.models import materias

class profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    email = models.EmailField()
    materia = models.ForeignKey(materias,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)
