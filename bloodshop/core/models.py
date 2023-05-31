from django.db import models

# Create your models here.

class Usuario (models.Model):

    rut                 = models.CharField(primary_key=True,max_length=10)
    nombre              = models.CharField(max_length=20)
    apellido            = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False,null=False)
    telefono            = models.CharField(max_length=45)
    email               = models.EmailField(unique=True,max_length=100, blank=True, null=True)
    contraseña          = models.PasswordField(max_length=30)

    def __str__(self) -> str:
        return self.nombreusuario
    
    
class Venta(models.Model):
    id_venta        = models.IntegerField(primary_key=True)
    fecha_venta     = models.DateField()
    total           = models.IntegerField()
    estado          = models.CharField(max_length=20)
    carrito         = models.IntegerField()

    def __str__(self) -> str:
        return self.Venta