from django import forms
from .models import Region, Usuario, TipoProducto, Productos, TipoAnimal, Animal
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroUser(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'direccion', 'region', 'cod_zip')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return password2

class LoginUser(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput)
