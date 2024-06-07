from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'pages/principal.html')

def mascotas(request):
    return render(request, 'pages/mascotas.html')

def perros(request):
    return render (request, 'pages/perros.html')

def gatos(request):
    return render (request, 'pages/gatos.html')