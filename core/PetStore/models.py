from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, db_column="idRegion")
    nombre = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return str(self.nombre)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, db_column="nombre")
    apellidos = models.CharField(max_length=100, db_column="apellidos")
    email = models.EmailField(unique=True, primary_key=True, db_column="email")
    pass1 = models.CharField(max_length=128, db_column="pass")
    direccion = models.CharField(max_length=255, db_column="direccion")
    region = models.ForeignKey("Region", on_delete=models.CASCADE, db_column="idRegion")
    codZip = models.CharField(max_length=20, db_column="codZip")
    
    def save(self, *args, **kwargs):
        # Antes de guardar, cifrar la contraseña si es nueva o modificada
        if self.pass1:
            self.pass1 = make_password(self.pass1)
        super().save(*args, **kwargs)

    def verificar_pass(self, pass1):
        # Verificar si la contraseña proporcionada coincide con la almacenada
        return check_password(pass1, self.pass1)

    def __str__(self):
        return self.email