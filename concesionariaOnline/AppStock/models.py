from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autos(models.Model):
    nombreUsuario= models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='autos', null=False)
    marca= models.CharField(max_length=20)
    modelo= models.CharField(max_length=20)
    año= models.IntegerField()
    kilometros= models.IntegerField()
    descripcion= models.CharField(max_length=250)
    precio= models.IntegerField()

    def __str__(self):
        return f'{self.marca} - {self.modelo}'

class Asesoramiento(models.Model):
    nombre= models.CharField(max_length=20)
    telefono= models.IntegerField()
    dataDeAsesoramiento= models.CharField(max_length=250)
    modeloDelAuto= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True)