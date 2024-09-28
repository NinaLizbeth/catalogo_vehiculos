from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def vehiculos_list(request):
    # Datos de ejemplo
    vehiculos = [
        {'marca': 'Ford', 'modelo': 'Focus', 'serial_carroceria': 'ABC123', 'serial_motor': 'XYZ789', 'categoria': 'particular', 'precio': 20000},
        {'marca': 'Chevrolet', 'modelo': 'Malibu', 'serial_carroceria': 'DEF456', 'serial_motor': 'UVW123', 'categoria': 'particular', 'precio': 25000},
        {'marca': 'Toyota', 'modelo': 'Corolla', 'serial_carroceria': 'GHI789', 'serial_motor': 'RST456', 'categoria': 'particular', 'precio': 22000},
    ]
    
    return render(request, 'vehiculo/vehiculos_list.html', {'vehiculos': vehiculos})

def tabla_vehiculos(request):
    return render(request, 'tabla.html', {})


def formulario_vehiculos(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el nuevo vehículo en la base de datos
            return redirect('vehiculos_list')  # Redirigimos después de guardar
    else:
        form = VehiculoForm()
    
    return render(request, 'formulario.html', {'form': form})