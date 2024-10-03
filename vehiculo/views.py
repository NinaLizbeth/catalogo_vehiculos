from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Marca
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


@login_required
def add_vehiculos(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el nuevo vehículo en la base de datos
            return redirect('vehiculos_list')  # Redirigimos después de guardar
    else:
        form = VehiculoForm()

    return render(request, 'add_vehiculo.html', {'form': form})


@login_required
def vehiculos_list(request):
    # Obtiene los parámetros de la consulta
    precio_min = request.GET.get('precio_min', 0)  # Por defecto es 0 si no se proporciona
    precio_max = request.GET.get('precio_max', None)  # Si no se proporciona, queda como None

    # Asegúrate de convertir los valores a enteros si son válidos
    try:
        precio_min = int(precio_min)
    except ValueError:
        precio_min = 0  # Valor por defecto si no es un entero válido

    if precio_max:
        try:
            precio_max = int(precio_max)
        except ValueError:
            precio_max = None  # Si no es válido, se ignora

    # Filtrar vehículos por precio
    if precio_max is not None:
        vehiculos = Vehiculo.objects.filter(precio__gte=precio_min, precio__lte=precio_max)
    else:
        vehiculos = Vehiculo.objects.filter(precio__gte=precio_min)

    return render(request, 'vehiculos_list.html', {'vehiculos': vehiculos})


def tabla_vehiculos(request):
    return render(request, 'tabla.html', {})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('index')  # Redirigir a la vista principal después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Plantilla de login
    redirect_authenticated_user = True  # Redirigir si ya está autenticado
    success_url = reverse_lazy('index')  # Redirigir al índice tras login
