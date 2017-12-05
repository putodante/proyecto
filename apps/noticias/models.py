from django.db import models

# Create your models here.
class noticias(models.Model):
    Titulo = models.CharField(max_length=50)
    Cuerpo = models.TextField(max_length=100)
    Logo = models.ImageField()

    def __str__(self):
        return self.Titulo