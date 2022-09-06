from mailbox import NoSuchMailboxError
#from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.
# por cada Tabla se crea una clase que que hereda de Models  Tabla cliente,Articulos,Pedidos, con sus 
# respectivos campos

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfono=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return 'nombre: %s seccion %s:  precio: %s' % (self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()






