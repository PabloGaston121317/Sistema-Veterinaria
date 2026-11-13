from django.db import models

class Cliente(models.Model):
    dni = models.IntegerField("DNI")
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    
    def __str__(self):
        return f" {self.dni} - {self.apellido}, {self.nombre}"

class Animal(models.Model):
    nombre = models.CharField(max_length=120)
    raza = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    duenio = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='animales')

    def __str__(self):
        return self.nombre + " " + self.raza
