from django import forms
from .models import Vehiculo, Marca
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'}),
        }

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 4:  # Cambia este número según tus necesidades
            raise forms.ValidationError("La contraseña debe tener al menos 4 caracteres.")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

class VehiculoForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), label="Marca")


    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    ]
    
    categoria = forms.ChoiceField(choices=CATEGORIAS, initial='Particular', label='Categoría')
    

    class Meta:
        model = Vehiculo
        fields = "__all__"
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }