# forms.py
from django import forms
from django.forms import ModelForm
from .models import Usuario
import re

class formsRegistro(ModelForm):
    REGIONES_CHILE =[
        ('RM', 'Región Metropolitana de Santiago'),
        ('1', 'Región de Tarapacá'),
        ('2', 'Región de Antofagasta'),
        ('3', 'Región de Atacama'),
        ('4', 'Región de Coquimbo'),
        ('5', 'Región de Valparaíso'),
        ('6', 'Región del Libertador General Bernardo O\'Higgins'),
        ('7', 'Región del Maule'),
        ('8', 'Región del Biobío'),
        ('9', 'Región de La Araucanía'),
        ('10', 'Región de Los Lagos'),
        ('11', 'Región de Aysén del General Carlos Ibáñez del Campo'),
        ('12', 'Región de Magallanes y de la Antártica Chilena'),
        ('14', 'Región de Los Ríos'),
        ('15', 'Región de Arica y Parinacota'),
        ('16', 'Región de Ñuble'),
    ]
    
    nombre = forms.CharField(max_length=100, required=True)
    apellidos = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    _pass = forms.CharField(widget=forms.PasswordInput, required=True)
    confirmar_pass = forms.CharField(widget=forms.PasswordInput, required=True)
    direccion = forms.CharField(max_length=255, required=True)
    region = forms.ChoiceField(choices=REGIONES_CHILE, required=True)
    
    class Meta:
        model = Usuario
        fields = "__all__"
    
    def clean_pass(self):
        _pass = self.cleaned_data.get("_pass")
        if len(_pass) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'\d', _pass):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return _pass
    
    def clean(self):
        cleaned_data = super().clean()
        _pass = cleaned_data.get("_pass")
        confirmar_pass = cleaned_data.get("confirmar_pass")

        if _pass and confirmar_pass:
            if _pass != confirmar_pass:
                raise forms.ValidationError("Las contraseñas no coinciden.")