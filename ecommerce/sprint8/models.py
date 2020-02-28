from django.db import models  
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
    descripcion = models.CharField(max_length=200,null=True)     
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True, related_name="productos")    
    imagen = models.ImageField(upload_to = 'img/', default = 'pic_folder/None/no-img.jpg')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
    
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
