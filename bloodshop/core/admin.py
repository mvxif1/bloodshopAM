from django.contrib import admin
from .models import Usuario, Venta,Producto

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(Producto)

