from rest_framework import serializers
from core.models import Venta, Usuario, Zapatilla, Marca



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['rut','nombre','apellido','fecha_nacimiento','telefono','email','contraseña']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields =['id_venta','fecha_venta','total','estado','carrito']

class ZapatillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapatilla
        fields =['id_producto','nombreproduct','tipo','descripcion','talla','cantidad','foto','precio','marcaproduct']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields =['codigoMarca','nombreMarca']