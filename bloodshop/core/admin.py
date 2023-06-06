from django.contrib import admin
from .models import Usuario, Venta, Marca, Zapatilla 

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(Marca)
admin.site.register(Zapatilla)

