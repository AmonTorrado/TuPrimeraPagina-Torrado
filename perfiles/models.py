from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =  models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    rol = models.CharField(max_length=40)
    imagen = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40,null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.profesion}"

#class PerfilUsuario(models.Model):
 #   CHOICE = (
  #      ('cliente', 'cliente'),
  #      ('vendedor', 'vendedor')
  #  )
   # usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
   # imagen = models.ImageField(upload_to='imagenes_usuarios')
    #rol = models.CharField(max_length=10, choices=CHOICE, null=True, blank=True)
    #
    #def __str__(self):
     #   return "Usuario: " + self.usuario.username + ", Rol del usuario: " + str(self.rol)