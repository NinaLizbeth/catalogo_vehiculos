from django.urls import path
from .views import index
from .views import vehiculos_list, tabla_vehiculos, formulario_vehiculos

urlpatterns = [
    path('', index, name='index'),  # '' hace que la vista index sea la vista principal
    path('vehiculos/', vehiculos_list, name='vehiculos_list'),
    path("tabla/", tabla_vehiculos, name="tabla" ),
    path("formulario/",  formulario_vehiculos, name="formulario"),
   
]
