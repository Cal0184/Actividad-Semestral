from django import forms
from .models import Region, Usuario, TipoProducto, Productos, tipoAnimal, Animal
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroUser(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'direccion', 'region', 'cod_zip')
        

class LoginUser(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput)
