from django.db import models

class Clase(models.Model):
    nombre_clase = models.CharField(max_length=200)

class Estudiante(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    nombre_estudiante = models.CharField(max_length=200)
    