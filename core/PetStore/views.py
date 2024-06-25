from django.shortcuts import render, redirect
from .models import Usuario, Region
from .forms import FormUser
from django.contrib.auth import authenticate,login,logout

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
        form = FormUser(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('principal')
    else:
        form = FormUser()
    return render(request, 'pages/registro.html', {'form': form})

def conectar(request):
    correo = request.POST["email"]
    password = request.POST["pass1"]
    user = authenticate(request,email=correo,password=password)
    if user is not None:
        login(request,user)
        if(request.user.is_authenticated):
            print("conectado")
        else:
            print("Fallo")
        return render(request,"pages/principal.html")
    else:
        print("No funciona")
        return render(request,"pages/principal.html")