from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Marca
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegistroUsuarioForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


@login_required
def add_vehiculos(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # guardar el nuevo vehículo 
            return redirect('vehiculos_list')  # redirijo a la tabla despues de guardar
    else:
        form = VehiculoForm()

    return render(request, 'add_vehiculo.html', {'form': form})


@login_required
def vehiculos_list(request):
  
    precio_min = request.GET.get('precio_min', 0)  # Por defecto es 0 si no se proporciona
    precio_max = request.GET.get('precio_max', None)  # Si no se proporciona, queda como None


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
            login(request, user)  # inicio sesion automáticamente después del registro
            return redirect('index')  # redirijo a la vista principal después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Plantilla de login
    redirect_authenticated_user = True  # redirige si ya estoy autenticada
    success_url = reverse_lazy('index')  # redirige al índice tdespues del login

#-----------------------------------Agregado--------------------------------------------------

@login_required(login_url='login')
@permission_required('vehiculo.view_vehiculo', raise_exception=True)
def ver_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'ver_vehiculo.html', {'vehiculo': vehiculo})


@login_required(login_url='login')
@permission_required('vehiculo.change_vehiculo', raise_exception=True)
def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado exitosamente.')
            return redirect('add_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'add_vehiculo.html', {'form': form, 'editing': True})

@login_required(login_url='login')
@permission_required('vehiculo.delete_vehiculo', raise_exception=True)
def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        messages.success(request, 'Vehículo eliminado exitosamente.')
        return redirect('vehiculos_list')
    return render(request, 'eliminar_vehiculo.html', {'vehiculo': vehiculo})




def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('index')  # Redirigir a la página de inicio
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registrar.html', {'form': form})