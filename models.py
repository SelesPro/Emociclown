

from django.db import models


class Taller(models.Model):
    titulo = models.CharField(max_length = 20, null = False)
    descripcion = models.TextField(blank = False,null = False)
    precio = models.FloatField(default = 10, null= True)
    aforo = models.IntegerField(default = 10, null= True)
    imagen = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.titulo
