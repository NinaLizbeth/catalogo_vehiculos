from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]


    marca=models.CharField(max_length=20 )
    modelo=models.CharField(max_length=100)
    serial_carroceria=models.CharField(max_length=50)
    serial_motor=models.CharField(max_length=50)
    categoria=models.CharField(max_length=20)
    precio=models.IntegerField()
    fecha_de_creacion=models.DateTimeField(auto_now_add=True) # auto_now_add se grega una sola vez
    fecha_de_modificacion=models.DateTimeField(auto_now=True) #auto_now se actualiza cada vez que modifica un objeto.

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.categoria}) - ${self.precio}"