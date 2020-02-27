from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30,null=True)


class Producto(models.Model):
    creacion = models.DateTimeField(auto_now_add=True,auto_now=False)
    nombre = models.CharField(max_length=50,null=True)
    precio = models.FloatField(null=True)
    ref = models.CharField(max_length=10,null=True)
    descripcion = models.CharField(max_length=200,null=True)
    #categoria = models.OneToManyRel(Categoria)

#class Cesta

#class Cliente
