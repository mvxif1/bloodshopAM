from django from forms
from django.forms import ModelForm
from .models import Zapatilla

class ZapatillaForm(ModelForm):

    class Meta:
        model = Zapatilla
        fields =['id_producto','nombreproduct','descripcion','foto','precio','marcaproduct']