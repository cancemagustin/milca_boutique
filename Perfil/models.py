from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con User
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)  # Evita duplicados
    direccion = models.TextField(blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True, unique=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username  # Muestra el nombre del usuario en el admin