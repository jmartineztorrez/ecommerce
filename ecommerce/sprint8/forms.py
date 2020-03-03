from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cesta

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1','password2']
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            'password1':'Contraseña',
            'password2':'Confirmar Contraseña',
        }
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre de Usuario',
                    'id': 'username'
                }
            ),            
            'first_name': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre',
                    'id': 'first_name'
                }
            ),            
            'last_name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese Apellidos',
                    'id':'last_name'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Email',
                    'id':'email'
                }
            ),
            'password1': forms.PasswordInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese Contraseña',
                    'id':'password1'
                }
            ),
            'password2': forms.PasswordInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Confirme Contraseña',
                    'id':'password2'
                }
            )
        }

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
