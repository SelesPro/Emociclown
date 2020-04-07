
from django.db import models


class Taller(models.Model):
    titulo = models.CharField(max_length = 20, null = False)
    descripcion = models.TextField(blank = False,null = False)
    precio = models.FloatField(default = 10, null= True)
    aforo = models.IntegerField(default = 10, null= True)
    fecha = models.DateField(default = 10, null = True)
    edad = models.IntegerField(default=10, null= True)  
    imagen = models.ImageField(upload_to='static/img')
    #agregar clave foranea de lugar 
    #agregar clave foranea de calendario


    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre1 = models.CharField(max_length = 20, null = False)
    telefono1 = models.IntegerField(default= 10, null= False)

    nombre_Happy = models.CharField(max_length = 20, null = False)
    telefono_Happy = models.IntegerField(default= 10, null= False)

    def __str__(self):
        return self.nombre1

class Campamento(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    descripcion = models.TextField(blank = False,null = False)
    #agregar clave foranea de calendario
    #agregar clave foranea de contacto 
    #agregar clave foranea de lugar  
     
     

class Evento_actividad(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    descripcion = models.TextField(blank = False,null = False)
    #agregar clave foranea de calendario
    #agregar clave foranea de contacto 
    #agregar clave foranea de lugar 



class Calendario(models.Model):
    #agregar claves foraneas de: talleres, eventos, actividades, cammpamentos y contacto
    mes = models.DateField(default = 10, null = True)
    dia = models.DateField(default = 10, null = True)
    hora = models.DateField(default = 10, null = True)
    anio = models.DateField(default = 10, null = True) 


class Lugar(models.Model):
    ubicacion = models.CharField(max_length = 20, null = False)


    #HAY QUE AGREGAR UNA CLASE "BLOG"????

    #de "OPINIONES y GALERIA" hay que crear registros???