from django.shortcuts import render, redirect
from .forms import formsRegistro
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
    return render(request, 'pages/registro.html')

def formRegistro(request):
    if request.method == 'POST':
        form = formsRegistro(request.POST)
        if form.is_valid():
            # Procesar datos
            return redirect('formRegistro')
    
    form = formsRegistro()   
    return render(request, 'pages/formRegistro.html', {'form': form})