from django.contrib import admin
from .models import Region, Usuario, TipoProducto, TipoAnimal, Productos, Animal
# Register your models here.
admin.site.register(Region)
admin.site.register(Usuario)
admin.site.register(TipoProducto)
admin.site.register(TipoAnimal)
admin.site.register(Animal)
admin.site.register(Productos)