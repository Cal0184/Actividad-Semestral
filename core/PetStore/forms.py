from django import forms
from .models import Region, Usuario

from django.forms import ModelForm

class FormUser(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pass1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    codZip = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuario
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['pass1'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['apellidos'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['codZip'].widget.attrs['class'] = 'form-control'