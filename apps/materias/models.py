from django.db import models

class materias(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre
# Create your models here.
