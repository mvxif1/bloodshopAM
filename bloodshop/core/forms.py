from django import forms
from .models import Zapatilla, Usuario

class ZapatillaForm(forms.ModelForm):

    class Meta:
        model = Zapatilla
        fields =['id_producto','nombreproduct','descripcion','foto','precio','marcaproduct']

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields =['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'email', 'contraseña']
    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        confclave = cleaned_data.get('confclave')

        if contraseña and confclave and contraseña != confclave:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

class DatosCompraForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    direccion = forms.CharField(label='Dirección')