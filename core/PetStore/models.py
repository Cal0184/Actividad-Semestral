from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    id_region = models.AutoField(primary_key=True, db_column="idRegion")
    nombre = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return str(self.nombre)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, db_column="nombre")
    apellidos = models.CharField(max_length=100, db_column="apellidos")
    email = models.EmailField(unique=True, primary_key=True, db_column="email")
    pass1 = models.CharField(max_length=128, db_column="contrasena")
    direccion = models.CharField(max_length=255, db_column="direccion")
    region = models.ForeignKey(Region, to_field='id_region', on_delete=models.SET_NULL, null=True, db_column="idRegion")
    codZip = models.CharField(max_length=20, db_column="codZip")
    
    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellidos)
        )