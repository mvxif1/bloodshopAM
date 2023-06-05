from rest_framework import serializers
from core.models import Venta, Usuario



 class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['rut','nombre','apellido','fecha_nacimiento','telefono','email','contraseña']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields =['id_venta','fecha_venta','total','estado','carrito']