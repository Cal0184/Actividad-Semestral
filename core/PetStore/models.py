from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, db_column="idRegion")
    nombre = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return str(self.nombre)
    
class Usuario(AbstractUser):
    direccion = models.CharField(max_length=255, db_column="direccion", blank=True, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, db_column="idRegion", blank=True, null=True)
    cod_zip = models.CharField(max_length=20, db_column="codZip", blank=True, null=True)
    

    def __str__(self):
        return (
            str (self.email)
            +" "
            +str (self.username)
            +" "
            +str(self.last_name))
    
class TipoProducto(models.Model):
    id_tipo = models.IntegerField(primary_key=True, db_column="idTipo")
    tipo = models.CharField(max_length=200, blank=False, null=False)
    
class Productos(models.Model):
    id_prod = models.IntegerField(unique=True, primary_key=True, db_column="idProducto")
    nombre = models.CharField(max_length=100, db_column="Nombre")
    desc = models.CharField(max_length=5000, db_column="Descripcion")
    precio = models.IntegerField(db_column="Precio")
    tipo = models.ForeignKey("TipoProducto", on_delete=models.CASCADE, db_column="Tipo")


class TipoAnimal(models.Model):
    id_tipo = models.IntegerField(unique=True, primary_key=True,db_column="Tipo_Animal")
    tipo = models.CharField(max_length=200,blank=False, null=False )

class Animal(models.Model):
    id_animal = models.IntegerField(unique=True, primary_key=True, db_column="idAnimal")
    tipo = models.ForeignKey("TipoAnimal", on_delete=models.CASCADE, db_column="Tipo")
    nombre = models.CharField(max_length=20, db_column="Nombre" )
    desc = models.CharField(max_length=5000, db_column="Descripcion")
    raza = models.CharField(max_length=50, db_column="Raza")

