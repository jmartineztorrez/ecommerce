from django.db import models

# Create your models here.
class Categoria(models.Model):
    creacion = models.DateTimeField(auto_now_add=True,auto_now=False)
    nombre = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    precio = models.FloatField(null=True)
    descripcion = models.CharField(max_length=200,null=True)
    categorias = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    passw = models.CharField(max_length=50,null=True)#revisar el field de password

    def __str__(self):
        return self.nombre


class Cesta (models.Model):
    cantidad =models.FloatField(null=True)
    total=models.FloatField(null=True)
    productos=models.ManyToManyField(Producto)
    clientes=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.cantidad




