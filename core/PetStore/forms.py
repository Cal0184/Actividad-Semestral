from django import forms
from .models import Region, Usuario

from django.forms import ModelForm

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['id_region', 'nombre']
        
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"