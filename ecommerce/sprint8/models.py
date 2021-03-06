from django.db import models
from django.contrib.auth.models import User 
from datetime import date
# Create your models here. 

class Categoria(models.Model):     
    nombre = models.CharField(max_length=50,null=True)      
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):         
        return self.nombre   

class Producto(models.Model):     
    nombre = models.CharField(max_length=50,null=True)     
    precio = models.FloatField(null=True) 
    stock = models.IntegerField(null=True)    
    descripcion = models.CharField(max_length=200,null=True)     
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True, related_name="productos")    
    imagen = models.ImageField(upload_to = 'static/images/', default = 'pic_folder/None/no-img.jpg')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
    
    def __str__(self):         
        return self.nombre  

#tabla temploral
class Cesta(models.Model): 
    cantidad =models.IntegerField(null=True)  
    productos=models.ForeignKey(Producto,on_delete=models.CASCADE,null=True)
    clientes=models.ForeignKey(User,on_delete=models.CASCADE,null=True)  
    sub_total=models.FloatField(null=True)
    estado=models.BooleanField(default=True,verbose_name='Estado')  

#inicia historial de venta 
class Factura(models.Model):
    clientes=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fecha= models.DateTimeField(auto_now_add=True, auto_now=False)

class Detalle_Factura(models.Model):
    cantidad =models.IntegerField(null=True)  
    productos=models.ForeignKey(Producto,on_delete=models.CASCADE,null=True)
    clientes=models.ForeignKey(User,on_delete=models.CASCADE,null=True)  
    sub_total=models.FloatField(null=True)
    estado=models.BooleanField(default=True,verbose_name='Estado')  
    codFact=models.ForeignKey(Factura,on_delete=models.CASCADE,null=True) 



