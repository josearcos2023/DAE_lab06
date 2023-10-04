from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    pub_date=models.DateTimeField("fecha de registro", auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(default=0)
    descripcion=models.CharField(default="",max_length=400)
    pub_date=models.DateTimeField("fecha de publicación",auto_now=True)

    def __str__(self):
        return self.nombre
    
