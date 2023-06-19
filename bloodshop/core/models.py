from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Usuario(models.Model):

    rut                 = models.CharField(primary_key=True,max_length=10)
    nombre              = models.CharField(max_length=20)
    apellido            = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False,null=False)
    telefono            = models.CharField(max_length=45)
    email               = models.EmailField(unique=True,max_length=100, blank=True, null=True)
    contraseña          = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre  

class Marca(models.Model):
    codigoMarca = models.AutoField(primary_key=True,verbose_name='Código de la zapatilla' )
    nombreMarca = models.CharField(null=True, max_length=25, blank=True)    

    def __str__(self) -> str:
        return self.nombreMarca

class Zapatilla(models.Model):
    id_producto     = models.IntegerField(primary_key=True)   
    nombreproduct   = models.CharField(max_length=30)
    tipo            = models.CharField(max_length=20)
    descripcion     = models.CharField(max_length=500)
    talla           = models.CharField(max_length=30)
    cantidad        = models.IntegerField()
    foto            = models.ImageField(upload_to="zapatillas")
    precio          = models.IntegerField()
    marcaproduct    = models.ForeignKey(Marca,on_delete=models.CASCADE)
        
    def __str__(self) -> str:
        return self.nombreproduct

    def get_absolute_url(self):
        return reverse('detailsmen1', kwargs={'pk': self.pk})


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    zapatilla = models.ForeignKey(Zapatilla, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.producto.precio * self.cantidad

class Venta(models.Model):
    id_venta        = models.IntegerField(primary_key=True)
    fecha_venta     = models.DateField()
    total           = models.IntegerField(10)
    estado          = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.Venta
    

