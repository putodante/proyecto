from django.contrib import admin

# Register your models here.
from apps.alumnos.models import Alumnos,Castigos

admin.site.register(Castigos)
admin.site.register(Alumnos)

