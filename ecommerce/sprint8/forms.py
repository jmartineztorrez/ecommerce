"""from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cantidad']
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
"""