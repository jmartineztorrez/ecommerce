from django import forms
from .models import Cesta

class CestaForm(forms.ModelForm):
    class Meta:
        model = Cesta
        fields = ['cantidad',]
        labels = {
            'cantidad': 'Cantidad de Producto'

        }
        widgets = {
            'cantidad': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'id': 'cantidad'
                }
            )
        }
