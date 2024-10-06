# vehiculo/models.py
from django.db import models
from django.contrib.auth.models import User



class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    # Remover las MARCAS y usar ForeignKey
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=[
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ])
    precio = models.IntegerField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar el catálogo de vehículos"),
        ]

    def __str__(self):
        return f"{self.marca}  {self.modelo} ({self.categoria}) - ${self.precio}"
