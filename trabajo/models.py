from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =  models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =  models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40,null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada =  models.IntegerField()

    def __str__(self):
        return self.nombre

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechadeentrega =  models.DateField(null=True, blank=True)
    entregado= models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    