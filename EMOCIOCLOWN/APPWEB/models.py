
from django.db import models


class Taller(models.Model):
    titulo = models.CharField(max_length = 20, null = False)
    descripcion = models.TextField(max_length = 300, null = False)
    imagen = models.ImageField(upload_to='static/img')
    
    def __str__(self):
        return self.titulo

class Calendario(models.Model):
    titulo = models.CharField(max_length = 20, null = False)
    descripcion = models.TextField(max_length = 300, null = False)
    imagen = models.ImageField(upload_to='static/img')
    aforo = models.IntegerField(default = 3, null= True)
    fecha = models.DateField(null=True, blank=True, auto_now_add=True)
    edad = models.IntegerField(default=10, null= True)
    precio = models.FloatField(default = 10, null= True) 

  
class Campamento(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    descripcion = models.TextField(max_length = 300,null = False)
    fecha_inicio = models.DateField(null=True, blank=True, auto_now_add=True)
    fecha_fin = models.DateField(null=True, blank=True, auto_now_add=True) #preguntar a Isa
    imagen = models.ImageField(upload_to='static/img')
  
 
class Opiniones(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    descripcion = models.TextField(blank = False,null = False)

class Galeria(models.Model):
    titulo = models.CharField(max_length = 50, null = False)
    descripcion = models.TextField(blank = False,null = False)
    imagen = models.ImageField(upload_to='static/img')


class Blog(models.Model):
    titular = models.CharField(max_length = 50, null = False)
    resumen = models.TextField(blank = False,null = False)
    descripcion = models.TextField(blank = False,null = False)
    fecha = models.DateField(null=True, blank=True, auto_now_add=True)
    tag = models.CharField(max_length = 50, null = False)
    imagen = models.ImageField(upload_to='static/img')       
        

class Datos_contacto(models.Model):
    nombre = models.CharField(max_length = 20, null = False)
    telefono = models.IntegerField(default= 9, null= False)
    email = models.EmailField(max_length = 50, null = False)
 

class Contacto(models.Model):
    nombre = models.CharField(max_length = 20, null = False)
    telefono = models.IntegerField(default= 9, null= False)
    email = models.EmailField(max_length = 50, null = False)
    asunto = models.CharField(max_length = 20, null = False)
    mensaje = models.TextField(blank = False, null = False)
     
     

  