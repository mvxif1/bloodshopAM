from django import forms
from .models import Zapatilla, Usuario

class ZapatillaForm(forms.ModelForm):

    class Meta:
        model = Zapatilla
        fields =['id_producto','nombreproduct','descripcion','foto','precio','marcaproduct']

