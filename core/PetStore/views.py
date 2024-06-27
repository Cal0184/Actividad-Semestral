from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroUser, LoginUser
from .models import Usuario, Region
from django.contrib.auth.decorators import login_required

# Create your views here.
def principal(request):
    return render(request, 'pages/principal.html')

def mascotas(request):
    return render(request, 'pages/mascotas.html')

def perros(request):
    return render(request, 'pages/perros.html')

def gatos(request):
    return render(request, 'pages/gatos.html')

def productos(request):
    return render(request, 'pages/productos.html')

def higiene(request):
    return render(request, 'pages/higiene.html')

def alimentos(request):
    return render(request, 'pages/alimentos.html')

def accesorios(request):
    return render(request, 'pages/accesorios.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('principal')
    else:
        form = RegistroUser()
    return render(request, 'registro.html', {'form': form})

def conectar(request):
    if request.method == 'POST':
        form = LoginUser(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('principal')
            else:
                form.add_error(None, 'Email o contraseña incorrectos.')
    else:
        form = LoginUser()
    return render(request, 'login.html', {'form': form})

@login_required
def desconectar(request):
    logout(request)
    return redirect('principal')