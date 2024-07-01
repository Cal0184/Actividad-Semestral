from django.urls import path
from . import views


urlpatterns = [
    path('', views.principal, name='principal'),
    path('mascotas', views.mascotas, name='mascotas'),
    path('perros', views.perros, name='perros'),
    path('gatos', views.gatos, name='gatos'),
    path('productos', views.productos, name='productos'),
    path('higiene', views.higiene, name='higiene'),
    path('accesorios', views.accesorios, name='accesorios'),
    path('alimentos', views.alimentos, name='alimentos'),
    path('registro', views.registro, name='registro'),
    path('login',views.conectar, name="login"),
    path('logout',views.desconectar, name='logout'),
    path('carrito', views.carrito, name='carrito'),
    ]